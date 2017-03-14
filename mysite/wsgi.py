"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
os.environ['DJANGO_SECRET_KEY'] = 'i5=1z$52s46ml_*d@ih(2-4z$miqz43osi@e8+5)$jg5mg-9x!'
os.environ['PUSHER_APP_ID'] = '311977'
os.environ['PUSHER_KEY'] = '7d21169e336fb7244895'
os.environ['PUSHER_SECRET'] = '7357f1380b714288bb23'
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
