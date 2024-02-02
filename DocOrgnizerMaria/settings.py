"""
Django settings for DocOrganizerMaria project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
AUTH_USER_MODEL = 'DocOrgnizer.UserProfile'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&qtxc=-s+mn8&li909c%7hf79i!_g*)h^6pos=ogk+2w@$sl!g"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'False'

ALLOWED_HOSTS = []

SSTATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

AUTHENTICATION_BACKENDS = [
    'DocOrgnizer.backends.CustomModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    'axes.backends.AxesStandaloneBackend',
]

# Application definition

INSTALLED_APPS = [
    "DocOrgnizer",
    # "django.contrib.admin",
    "useraccount",
    "django.contrib.auth",
    'dbbackup',
    'axes',
    'csp',
    "django_recaptcha",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django_auto_logout.middleware.auto_logout',
    'axes.middleware.AxesMiddleware',
    'csp.middleware.CSPMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 31536000  # 1 year


CSP_DEFAULT_SRC = ("'self'", )
CSP_IMG_SRC = ("'self'", 'https://www.google.com')
CSP_CONNECT_SRC = ("'self'", 'https://www.google.com')
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", 'https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css','https://unpkg.com', 'https://stackpath.bootstrapcdn.com')  # Allow inline styles and Bulma CSS
CSP_SCRIPT_SRC = ("'self'", 'https://www.google.com', 'https://www.gstatic.com', "'unsafe-inline'", 'https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/js/bulma.min.js', 'https://ajax.googleapis.com', 'https://unpkg.com', 'https://stackpath.bootstrapcdn.com')
CSP_FRAME_SRC = ("'self'", 'https://www.google.com')
CSP_FONT_SRC = ("'self'", 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css')
CSP_FONT_SRC = ("'self'", "https://use.fontawesome.com")
CSP_FONT_SRC = ("'self'", 'https://stackpath.bootstrapcdn.com')
import os



DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': f"{BASE_DIR}/DocOrganizerbackup/"}
DBBACKUP_CLEANUP_KEEP = 10  # Number of backups to keep
DBBACKUP_CLEANUP_KEEP_MEDIA = 5  # Number of media backups to keep

LOGIN_URL = 'login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AXES_FAILURE_LIMIT = 2  # Limit login attempts to 5
AXES_COOLOFF_TIME = 10  # Lock out the user for 1 minute after reaching the limit
 

AUTO_LOGOUT = {'IDLE_TIME': 180 , 'REDIRECT_TO_LOGIN_IMMEDIATELY': True,'MESSAGE': 'The session has expired. Please login again to continue.',}

SESSION_ENGINE = 'django.contrib.sessions.backends.db' 
ROOT_URLCONF = "DocOrgnizerMaria.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                'django_auto_logout.context_processors.auto_logout_client',
               
            ],
        },
    },
]

WSGI_APPLICATION = "DocOrgnizerMaria.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

# settings.py
RECAPTCHA_PUBLIC_KEY = '6Ldm1V4pAAAAAHl8heLdDquWuFhEwLRasuxpu5e5'
RECAPTCHA_PRIVATE_KEY = '6Ldm1V4pAAAAAAXRldyxrVPQ3kqV9tJKbI-tEhj6'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

AUTH_PASSWORD_VALIDATORS = [
    # Existing validators...
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
    {
        'NAME': 'DocOrgnizer.validators.IsEntireAlphaPasswordValidator',
    },
    {
        'NAME': 'DocOrgnizer.validators.HasUpperCasePasswordValidator',
    },
    {
        'NAME': 'DocOrgnizer.validators.HasLowerCasePasswordValidator',
    },
    {
        'NAME': 'DocOrgnizer.validators.HasNumberPasswordValidator',
    },
    {
        'NAME': 'DocOrgnizer.validators.HasSpecialCharacterPasswordValidator',
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'docorganizerteam@gmail.com'
EMAIL_HOST_USER = 'docorganizerteam@gmail.com'
EMAIL_HOST_PASSWORD ='gvdw bift vitn uqpk'
EMAIL_PORT = 587
EMAIL_USE_TLS = True




ENCRYPTION_KEY = b'\x19\x8a\xf1\x04]\xc9"5%=}\xf4\xb5\xa5\x03\xde\xf1^M\x00\x92\x8a\xa8\xa0\x95\xc2\xab\xe1\xf6D\x96u'

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

FORMATTERS = (
    {
        "verbose": {
            "format": "{levelname} {asctime:s} {name} {threadName} {thread:d} {module} {filename} {lineno:d} {name} {funcName} {process:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {asctime:s} {name} {module} {filename} {lineno:d} {funcName} {message}",
            "style": "{",
        },
    },
)


HANDLERS = {
    "console_handler": {
        "class": "logging.StreamHandler",
        "formatter": "simple",
        "level": "DEBUG"
    },
    "info_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": f"{BASE_DIR}/logs/DocOrgnizer_info.log",
        "mode": "a",
        "encoding": "utf-8",
        "formatter": "verbose",
        "level": "INFO",
        "backupCount": 5,
        "maxBytes": 1024 * 1024 * 5,  # 5 MB
    },
    "error_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": f"{BASE_DIR}/logs/DocOrgnizer_error.log",
        "mode": "a",
        "formatter": "verbose",
        "level": "WARNING",
        "backupCount": 5,
        "maxBytes": 1024 * 1024 * 5,  # 5 MB
    },
}

LOGGERS = (
    {
        "django": {
            "handlers": ["console_handler", "info_handler"],
            "level": "INFO",
        },
        "django.request": {
            "handlers": ["error_handler"],
            "level": "INFO",
            "propagate": True,
        },
        "django.template": {
            "handlers": ["error_handler"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.server": {
            "handlers": ["error_handler"],
            "level": "INFO",
            "propagate": True,
        },
    },
)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": FORMATTERS[0],
    "handlers": HANDLERS,
    "loggers": LOGGERS[0],
}
