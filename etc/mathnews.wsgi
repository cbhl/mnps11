import os
import sys

path = '/opt/mnps11'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mathnews.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
