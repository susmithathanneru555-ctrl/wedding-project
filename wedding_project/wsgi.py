"""Compatibility shim for deployments using the original project name.

The Render deployment logs reveal that Gunicorn continues to attempt importing
``wedding_project.wsgi`` even though the real Django package is
`wedding_invitation`.

This module simply re‑exports the application from the renamed package, so
both of the following will work:

    gunicorn wedding_invitation.wsgi:application
    gunicorn wedding_project.wsgi:application  # now also valid

The presence of this package means no further configuration overrides are
required on the Render side; the repo itself now contains a module named
`wedding_project`.
"""

from wedding_invitation.wsgi import application  # noqa: F401
