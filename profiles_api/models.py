import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class UserProfileManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, name, password=None):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Please enter an email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    date_of_creation = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    objects = UserProfileManager()

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email


class Capsule(models.Model):
    capsule_name = models.CharField(max_length=255)
    capsule_text = models.TextField(max_length=360, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    date_published = models.DateField(blank=False, null=True)

    def __str__(self):
        return self.capsule_name


class CapsuleImage(models.Model):
    capsule_file = models.FileField(blank=True, null=True,
                                    upload_to='media/covers/%Y/%m/%D/')

    gallery_capsule = models.ForeignKey(Capsule, related_name='images', on_delete=models.CASCADE)


