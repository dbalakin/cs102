


from .base import *

DEBUG = True
INSTALLED_APPS += ['django.contrib.postgres',]
DATABASES = {
     'default': {
     'ENGINE': 'django.db.backends.postgresql_psycopg2',
     'NAME': 'postgres',
     'USER': 'postgres',
     'PASSWORD':'',
     'HOST': 'db',
     'PORT': 5432,
     }
}