from .settings import *
import dj_database_url


DEBUG = False
DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['pyramide-services.com']

 
MIDDLEWARE += 'whitenoise.middleware.WhiteNoiseMiddleware',

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
