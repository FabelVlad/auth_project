import os

import environ

BASE_DIR = environ.Path(__file__) - 2
APPS_DIR = BASE_DIR.path('apps')

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    DJANGO_SECRET_KEY=(str, ''),
    # DJANGO_ADMINS=(list, []),
    DJANGO_ALLOWED_HOSTS=(list, []),
    DJANGO_STATIC_ROOT=(str, str(APPS_DIR('staticfiles'))),
    DJANGO_MEDIA_ROOT=(str, str(APPS_DIR('media'))),
    DJANGO_DATABASE_URL=(str, f'sqlite:////{str(BASE_DIR)}\\multi_auth_sqlite.db'),
    DJANGO_EMAIL_HOST=(str, ''),
    DJANGO_EMAIL_PORT=(int, 25),
    DJANGO_EMAIL_HOST_USER=(str, ''),
    DJANGO_EMAIL_HOST_PASSWORD=(str, ''),
    DJANGO_EMAIL_USE_TLS=(bool, False),
    # DJANGO_EMAIL_USE_SSL
    # DJANGO_EMAIL_TIMEOUT
    # DJANGO_EMAIL_SSL_KEYFILE
    # DJANGO_EMAIL_SSL_CERTFILE
    DJANGO_AWS_ACCESS_KEY_ID=(str, ''),
    DJANGO_AWS_SECRET_ACCESS_KEY=(str, ''),
    DJANGO_AWS_STORAGE_BUCKET_NAME=(str, ''),
    DJANGO_AWS_S3_OBJECT_PARAMETERS=(dict, {'CacheControl': 'max-age=86400'}),
    DJANGO_AWS_S3_FILE_OVERWRITE=(bool, True),
    DJANGO_AWS_LOCATION=(str, ''),
    DJANGO_AWS_DEFAULT_ACL=(str, ''),
)

environ.Env.read_env(env_file=os.path.join(str(BASE_DIR), '.env'))

SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

    'storages'
]

LOCAL_APPS = [
    'apps.profiles.apps.ProfilesConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': env.db('DJANGO_DATABASE_URL')
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Mail settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = env('DJANGO_EMAIL_HOST')
EMAIL_PORT = env.int('DJANGO_EMAIL_PORT')
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env.bool('DJANGO_EMAIL_USE_TLS')
# EMAIL_USE_SSL
# EMAIL_TIMEOUT
# EMAIL_SSL_KEYFILE
# EMAIL_SSL_CERTFILE

# Allauth settings

SOCIALACCOUNT_ADAPTER = 'apps.profiles.my_adapter.SocialAccountAdapter'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
LOGIN_REDIRECT_URL = 'profile'
LOGIN_URL = 'account_login'
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_USERNAME_BLACKLIST = ['admin']

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
    {
        'NAME': 'apps.common.validators.MaximumLengthValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
# STATIC_ROOT = env('DJANGO_STATIC_ROOT')

# MEDIA_URL = '/media/'
# MEDIA_ROOT = env('DJANGO_MEDIA_ROOT')

STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

DEFAULT_FILE_STORAGE = 'apps.common.custom_storage.MediaStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# S3 settings

AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_S3_OBJECT_PARAMETERS = env.dict('DJANGO_AWS_S3_OBJECT_PARAMETERS')
AWS_S3_FILE_OVERWRITE = env.bool('DJANGO_AWS_S3_FILE_OVERWRITE')
AWS_LOCATION = env('DJANGO_AWS_LOCATION')
AWS_DEFAULT_ACL = env('DJANGO_AWS_DEFAULT_ACL')

# AWS Permission CORS settings

'''
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
'''
