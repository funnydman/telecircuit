try:
    from .base import *
except ImportError:
    raise ImportError(
        "Can't find the file with basic settings. Did you import?")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST_NAME'),
        'PORT': '',
    }
}

DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')

SECRET_KEY = os.environ.get('SECRET_KEY')
