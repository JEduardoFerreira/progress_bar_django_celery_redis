from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(Path(__file__).resolve().parent)

APP_DIR = BASE_DIR + '/service/'

SITIO_DIR = BASE_DIR + '/progress/'



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3(%iv5pix=2(s$)i3-gi^jo10*cpu!r11hyli2r06s+f(h!%79'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'service',
    'django_celery_results',
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

ROOT_URLCONF = 'progress.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(APP_DIR, 'templates'),
            os.path.join(SITIO_DIR, 'templates'),
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

WSGI_APPLICATION = 'progress.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

NAME_BD = 'celery_progress'

USER_BD = 'root'

PASSWORD_BD = 'es220800'

HOST_BD = '127.0.0.1'

DATABASES = {
    'default': {
        # Mecanismo de acesso ao banco de daods. 
        # (Pode utilizado 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle').
        'ENGINE': 'django.db.backends.mysql',
        # Nome do banco de dados
        'NAME': NAME_BD,
        # Usuário do banco de dados
        'USER': USER_BD,
        # Senha de acesso do usuário acima ao banco de dados
        'PASSWORD': PASSWORD_BD,
        # Endereço do banco de dados
        'HOST': HOST_BD, # Localhost
        # Porta do banco de dados (padrão: 3306)
        'PORT': '', # Porta padrão para acesso ao banco de dados local(3306)
    }
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

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'

#CELERY_BROKER_URL = 'db+mysql://root:es220800@127.0.0.1/celery_progress'

CELERY_ACECPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_BACKEND = 'django-db'

# mysql
#CELERY_RESULT_BACKEND = 'db+mysql://root:es220800@127.0.0.1/celery_progress'

#CELERY_RESULT_BACKEND = 'database'

# # use custom schema for the database result backend.
# database_table_schemas = {
#     'task': 'celery',
#     'group': 'celery',
# }

# # use custom table names for the database result backend.
# database_table_names = {
#     'task': 'myapp_taskmeta',
#     'group': 'myapp_groupmeta',
# }