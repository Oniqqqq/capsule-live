from rest_framework import serializers

from profiles_api.models import UserProfile

from rest_auth.serializers import PasswordResetSerializer
from allauth.account.forms import ResetPasswordForm


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name',  'date_of_creation']


class PasswordSerializer (PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm