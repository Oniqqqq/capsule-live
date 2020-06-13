from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text

from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError

from rest_auth.models import TokenModel
from rest_auth.utils import import_callable

from profiles_api.models import UserProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'first_name', 'last_name', 'spouse_name', 'date_of_birth']