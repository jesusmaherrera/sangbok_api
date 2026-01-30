import os

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-%*=5%im@0#p@1mwr_ck2&hsbk%qatk6-$c$fl9$i)rkbk%d)ju')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# En Dokploy: define ALLOWED_HOSTS (ej. "tu-dominio.com,api.tu-dominio.com") o usa "*" para aceptar todo
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')