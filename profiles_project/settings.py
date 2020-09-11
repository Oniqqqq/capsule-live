"""
Django settings for profiles_project project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's(^ac6+$keq1jp46z-bdx6q%2j_wncz!=x_p9az3xjta9hw&m-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', '.herokussl.com', '*.herokussl.com', '*.herokuapp.com', '.yourtimecapsule.live']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
    'allauth.socialaccount.providers.google',
    'storages',
    'profiles_api',
    'push_notifications',




]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'profiles_project.urls'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'profiles_api/templates'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'profiles_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'capsule',
        'USER': 'postgres',
        'PASSWORD': '1337113371zZ',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'capsules',
        'USER': 'djalilcapsule',
        'PASSWORD': '1337113371gH',
        'HOST': 'database-1.cjfxe7mosmma.eu-north-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'static'),

]


MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

AUTH_USER_MODEL = 'profiles_api.UserProfile'


REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'profiles_api.serializers.UserSerializer',

}


REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%d/%m/%Y %H:%M:%S",
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],

        # Only enable JSON renderer by default.
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]

}




ACCOUNT_USER_MODEL_USERNAME_FIELD = 'name'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_AUTHENTICATION_METHOD = 'name'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 15
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/verification=1'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/verification=1'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1


SITE_ID = 1
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@yourtimecapsule.live'
EMAIL_HOST = 'smtp.eu.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'postmaster@mg.yourtimecapsule.live'
EMAIL_HOST_PASSWORD = 'f2eeecb547031b8704b7beaf137cf6b0-07e45e2a-57c71a95'



AWS_ACCESS_KEY_ID = 'AKIARJQ6CH3VJQGKZG7H'
AWS_SECRET_ACCESS_KEY = 'Hnq5nKV/jz0rtBp7T6QAyZmzn4lBk12DtZfaBZLJ'
AWS_STORAGE_BUCKET_NAME = 'yourtimecapsule'
AWS_S3_REGION_NAME = 'eu-north-1'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

'''
PUSH_NOTIFICATIONS_SETTINGS = {
  # Load and process all PUSH_NOTIFICATIONS_SETTINGS using the AppConfig manager.
  "CONFIG": "push_notifications.conf.AppConfig",

  "APPLICATIONS": {
        "TimeCapsule": {
            "PLATFORM": "APNS",
            'HOST': 'api.sandbox.push.apple.com',
            "CERTIFICATE": "PushCertificate.pem",
            "TOPIC": 'com.khdenis.TimeCapsule',
                },
  }

}


'''


PUSH_NOTIFICATIONS_SETTINGS = {

        "APNS_CERTIFICATE": "PushCertificate.pem",
        "APNS_TOPIC": "com.khdenis.TimeCapsule",
        "UPDATE_ON_DUPLICATE_REG_ID": 'True',
        "APNS_USE_SANDBOX ": "False",
}