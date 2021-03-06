"""
Django settings for HTSP project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from environs import Env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = Env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

_host = env.str('HOST', '')

if _host:
    ALLOWED_HOSTS.append(_host)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',

    'authentication',
    'products',
    'orders',
    'reports',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HTSP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'HTSP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('POSTGRES_DB', ''),
        'USER': env.str('POSTGRES_USER', ''),
        'PASSWORD': env.str('POSTGRES_PASSWORD', ''),
        'HOST': env.str('POSTGRES_HOST', 'localhost'),
        'PORT': env.int('POSTGRES_PORT', 5432),
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_EXPIRY_HOURS = env.int('SESSION_EXPIRY_HOURS', 2)

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

DJANGO_LOG_PATH = env.str('DJANGO_LOG_PATH', os.path.join(BASE_DIR, ".data/django/django.log"))
CELERY_LOG_PATH = env.str('CELERY_LOG_PATH', os.path.join(BASE_DIR, ".data/django/celery.log"))

if not os.path.exists(os.path.dirname(DJANGO_LOG_PATH)):
    os.makedirs(os.path.dirname(DJANGO_LOG_PATH))

if not os.path.exists(os.path.dirname(CELERY_LOG_PATH)):
    os.makedirs(os.path.dirname(CELERY_LOG_PATH))

LOGFILE_SIZE = 5 * 1024 * 1024

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'base': {
            'format': '{levelname} | {asctime} | {module} | {process:d} | {thread:d} | {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'base_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': DJANGO_LOG_PATH,
            'maxBytes': LOGFILE_SIZE,
            'formatter': 'base'
        },
        'celery_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': CELERY_LOG_PATH,
            'maxBytes': LOGFILE_SIZE,
            'formatter': 'base'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'base_file'],
            'level': env.log_level('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True
        },
        'celery': {
            'handlers': ['console', 'celery_file'],
            'level': env.log_level('CELERY_LOG_LEVEL', 'INFO'),
            'propagate': True
        },
    },
}

DEFAULT_DATE_FORMAT = '%d-%m-%Y'

AUTH_USER_MODEL = 'authentication.User'
LOGIN_URL = 'auth:login'
LOGIN_REDIRECT_URL = 'dashboard'
# LOGOUT_REDIRECT_URL = 'registration:login'

# CELERY_BROKER_URL = env.str('BROKER_URL')
# CELERY_TASK_SOFT_TIME_LIMIT = env.int('TASK_SOFT_TIME_LIMIT_SEC', 60)
