#!/usr/bin/env python
"""
Entry point for Render deployment
"""
import os
import sys

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding_invitation.settings')

# Setup Django
import django
django.setup()

# Import the WSGI application
from wsgi import application

if __name__ == '__main__':
    # This allows running the script directly for testing
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)