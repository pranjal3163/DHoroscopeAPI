from DHoroscopeCrawler.settings.common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['0.0.0.0', '52.24.58.174']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dHoroscope',
        'USER': 'pranjal',
        'PASSWORD': 'Pranjal3163#',
        'HOST': 'dhoro.c9w15j0y13hj.us-west-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode = 'STRICT_TRANS_TABLES'"
        }
    }

}
