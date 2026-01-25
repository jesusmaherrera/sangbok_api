# Sangbok API

Proyecto Django básico para API de canciones.

## Requisitos

- Python 3.10 o superior
- Django 6.0

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
```bash
# En Windows
venv\Scripts\activate

# En Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones:
```bash
python manage.py migrate
```

5. Crear un superusuario (opcional):
```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor de desarrollo:
```bash
python manage.py runserver
```

El proyecto estará disponible en `http://127.0.0.1:8000/`

## Producción / Deploy

Para producción, usa Gunicorn con la configuración que escucha en `0.0.0.0`:

### Opción 1: Usando el archivo de configuración
```bash
gunicorn -c gunicorn_config.py
```

### Opción 2: Comando directo
```bash
gunicorn --bind 0.0.0.0:8000 sangbok_api.wsgi:application
```

**Importante para Dokploy**: Asegúrate de que el comando de inicio en Dokploy use `0.0.0.0` en lugar de `127.0.0.1`. El archivo `gunicorn_config.py` ya está configurado correctamente.

## Estructura del Proyecto

```
sangbok_api/
├── manage.py
├── requirements.txt
├── sangbok_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── README.md
```

