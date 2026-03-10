#!/usr/bin/env python
"""
WSGI config for wedding invitation project.
"""
import os
import sys

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Set environment variables from Render
os.environ.setdefault('SECRET_KEY', 'pRI1De1BYigviqXLgXUi8ToVmO3tbp1DX6depQF2dbrVMFuM9hrDqzpH_XcsXjImLm4')
os.environ.setdefault('DEBUG', 'False')
os.environ.setdefault('ALLOWED_HOSTS', '*.onrender.com,localhost,127.0.0.1')

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding_invitation.settings')

# Import Django and setup
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

print("WSGI application loaded successfully", file=sys.stderr)