web: python manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 120 sangbok_api.wsgi:application
