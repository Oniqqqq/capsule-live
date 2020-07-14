from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text

from rest_framework import serializers, exceptions, fields
from rest_framework.exceptions import ValidationError

from rest_auth.models import TokenModel
from rest_auth.utils import import_callable

from profiles_api.models import UserProfile
from profiles_api import models

# Get the UserModel
UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'email','name' , 'date_of_creation']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username_email(self, username, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        elif username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include either "username" or "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = None

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings

            # Authentication through email
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:
                user = self._validate_email(email, password)

            # Authentication through username
            elif app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
                user = self._validate_username(username, password)

            # Authentication through either username or email
            else:
                user = self._validate_username_email(username, email, password)

        else:
            # Authentication without using allauth
            if email:
                try:
                    username = UserModel.objects.get(email__iexact=email).get_username()
                except UserModel.DoesNotExist:
                    pass

            if username:
                user = self._validate_username_email(username, '', password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    email_address.send_confirmation(
                        request=self.context.get('request')
                    )
                    raise serializers.ValidationError(_('E-mail is not verified.'))

        attrs['user'] = user
        return attrs


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = TokenModel
        fields = ('key',)

class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('email', )


class JWTSerializer(serializers.Serializer):
    """
    Serializer for JWT authentication.
    """
    token = serializers.CharField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        """
        Required to allow using custom USER_DETAILS_SERIALIZER in
        JWTSerializer. Defining it here to avoid circular imports
        """
        rest_auth_serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})
        JWTUserDetailsSerializer = import_callable(
            rest_auth_serializers.get('USER_DETAILS_SERIALIZER', UserDetailsSerializer)
        )
        user_data = JWTUserDetailsSerializer(obj['user'], context=self.context).data
        return user_data


class CapsuleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CapsuleImage
        fields = ('capsule_file', )


class SharedToSerializer(serializers.ModelSerializer):
    shared_to = serializers.SlugRelatedField(queryset=models.UserProfile.objects.all(), slug_field='name', many=True)
    class Meta:
        models = models.UserProfile
        fields = ('shared_to',)



from datetime import date, timedelta


class CapsuleSerializer(serializers.ModelSerializer):

    now = timezone.now() + timedelta(hours=1)

    date_to_open_back = fields.DateTimeField(format='%d/%m/%Y %H:%M:%S', default=now)
    date_to_open = fields.DateTimeField(format='%d/%m/%Y %H:%M:%S', required=True)
    images = CapsuleImageSerializer(many=True, read_only=True)
    shared_to = serializers.SlugRelatedField(queryset=models.UserProfile.objects.all(), slug_field='name', many=True)

    def validate(self, data):
        # The keys can be missing in partial updates

        if 'date_to_open_back' in data and 'date_to_open' in data:
            if (data['date_to_open_back'] + timedelta(hours=1)) >= (data['date_to_open'] + timedelta(hours=0)):
                raise serializers.ValidationError({
                    'date_to_open': 'date of opening cannot be earlier than 1 hour after creations date',
                })
        return super(CapsuleSerializer, self).validate(data)

    class Meta:
        model = models.Capsule
        fields = ('id', 'capsule_name', 'capsule_text', 'created_on', 'date_to_open_back', 'date_to_open', 'shared_to', 'images', )
        
    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        owner_id = self.context['request'].user.id
        shared_to = validated_data.pop('shared_to')

        gallery_capsule = models.Capsule.objects.create(capsule_name=validated_data.get('capsule_name', 'no-capsule_name'), capsule_text=validated_data.get('capsule_text'), date_to_open_back=validated_data.get('date_to_open_back'), date_to_open=validated_data.get('date_to_open'),
                                                        owner_id=owner_id)
        gallery_capsule.save()
        for data in shared_to:
            gallery_capsule.shared_to.add(data)
        gallery_capsule.save()

        for image_data in images_data.values():
            models.CapsuleImage.objects.create(gallery_capsule=gallery_capsule, capsule_file=image_data)
        return gallery_capsule


class OpenedCapsuleListSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = models.Capsule
        fields = ('id', 'capsule_name', 'date_to_open', 'owner')


class ClosedCapsuleListSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = models.Capsule
        fields = ('id', 'capsule_name', 'date_to_open', 'owner')


class ExistUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('name',)