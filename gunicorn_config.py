"""Configuración de Gunicorn para producción"""
import multiprocessing

# Dirección y puerto donde escuchará el servidor
bind = "0.0.0.0:8000"

# Número de workers (procesos)
workers = multiprocessing.cpu_count() * 2 + 1

# Timeout
timeout = 30

# Logging
accesslog = "-"  # Log a stdout
errorlog = "-"  # Log a stderr
loglevel = "info"

# Nombre de la aplicación WSGI
wsgi_app = "sangbok_api.wsgi:application"
