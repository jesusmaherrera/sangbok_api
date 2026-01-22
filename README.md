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

