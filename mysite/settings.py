import os
import tempfile
import django


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'i!vp3!w3&+e0_cvd1@w)c5ecld^hloi(x!ytz&%-hey46gvq7o'

DEBUG = True

ALLOWED_HOSTS = ['astaroth.pythonanywhere.com']

INSTALLED_APPS = (

    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'blog',
    'mathfilters',
    'ckeditor',
    'sass_processor',
    'pipeline',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

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
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Samara'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'extra-styles/scss'),
    os.path.join(BASE_DIR, 'node_modules'),
]

SASS_INCLUDE_DIR = BASE_DIR + '/static/scss/'
# PIPELINE['SASS_BINARY'] = '/usr/bin/env sassc --load-path ' + SASS_INCLUDE_DIR
SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'

MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = "static/media/uploads/"

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [['Source', 'Link', 'Unlink',
                     'SpecialChar, Autogrow, SimpleLink, SimpleImage, smiley, image, dialog, forms, preview, table, tableresize, tabletools']],
    },
}


SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Astaroth Blog',

    # search
    'SEARCH_URL': '',

    # menu
    'MENU': (
        {
            'app': 'blog',
            'icon': 'icon-file',
            'models': (
                'BlogConfig',
                'BlogPost',
                'Tag',
                'page_settings',
            )
        },

        '-',
        {
            'app': 'backups',
            'icon': 'icon-hdd',
            'permissions': 'users.admin_menu',
        },
        {
            'app': 'admin',
            'icon': 'icon-list-alt',
            'permissions': 'users.admin_menu',
        },
    ),
}