"""
WSGI config for DHoroscopeCrawler project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import loadenv


from django.core.wsgi import get_wsgi_application

loadenv.getenvironment()

application = get_wsgi_application()