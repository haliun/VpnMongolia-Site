"""
Django settings for vpndjango project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9#($a76_h(my87t+j+^-jsif2ad9@yxn@u=)_2(#fgdr0p(g%9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mongol.world','153.127.249.210','www.mongol.world','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'bootstrap3',
    'django_forms_bootstrap',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'openvpn',
    'registration',
    'django.contrib.admin',





]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'sitevpn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sitevpn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'openvpn',
        'USER': 'root',
        'PASSWORD': 'uragshaa',
       # 'HOST': '/var/lib/mysql/mysql.sock',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'
LANGUAGES = [
  ('ru', _('Russia')),
  ('en', _('English')),
  ('mn', _('Mongolian')),
]
LOCALE_PATHS = (
    'locale',
    # os.path.join(PROJECT_DIR, 'locale'),
)
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
DEFAULT_CONTENT_TYPE='x'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__)) + "/../"
#MEDIA_ROOT='/data/mysite/openvpn/openvpn/media/'

MEDIA_URL='/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join( PROJECT_DIR, "static" ),
)
STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
#DEFAULT_FROM_EMAIL = 'vpnmongoliafree@gmail.com'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER = 'vpnmongoliafree@gmail.com'
EMAIL_HOST_PASSWORD = 'uragshaa'
EMAIL_USE_TLS = True
EMAIL_PORT = '587'

###############################
REGISTRATION_OPEN = True        # Если равно True, то пользователи могут регистрироваться
ACCOUNT_ACTIVATION_DAYS = 7     # время в течении которого можно активировать аккаунт;
                                # в качестве примера выбрано 7 дней или одна неделя, но Вы можете указать другое значение.
REGISTRATION_AUTO_LOGIN = True  # Если равно  True, то пользователь будет автоматически входить в систему.
LOGIN_REDIRECT_URL = '/'  # Страница, на которую будут попадать пользователи, после успешного входа в систему.
LOGIN_URL = '/accounts/login/'  # Страница, на которую перенаправляются пользователи, если они не вошли в систему и
                                # пытаются получить доступ к страницам, которые требуют аутентификации