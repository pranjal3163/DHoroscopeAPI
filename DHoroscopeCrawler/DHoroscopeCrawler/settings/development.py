from DHoroscopeCrawler.settings.common import *

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ["127.0.0.1","192.168.1.6"]


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dHoroscope',
        'USER': 'dbadmin',
        'PASSWORD': 'pranjal3163#',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode = 'STRICT_TRANS_TABLES'"
        }
    }
}
