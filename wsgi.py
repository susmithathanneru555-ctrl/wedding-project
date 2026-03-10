#!/usr/bin/env python
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.getcwd())

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding_invitation.settings')

# Import and run Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()