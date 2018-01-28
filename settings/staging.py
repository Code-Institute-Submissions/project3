
from base import *
#import dj_database_url
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #dj_database_url.config('CLEARDB_DATABASE_URL'),
    }
}


# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://project3-unicorn.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'frscollo@hotmail.com'

SITE_URL = 'https://project3-unicorn.herokuapp.com'
ALLOWED_HOSTS.append('project3-unicorn.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
