from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_site',
        'USER': 'root',
        'PASSWORD':'nicoRoot123',
        'HOST':'localhost',
        'PORT':'33060',
        
    }
}