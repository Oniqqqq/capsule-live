from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.permissions import (AllowAny)
from allauth.account.models import EmailAddress
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response
from rest_framework import status

