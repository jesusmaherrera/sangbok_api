# Sangbok API - Django Application

Aplicación Django básica configurada para deploy en Dokploy.

## Configuración para Dokploy

### Variables de Entorno Necesarias

En la configuración de tu aplicación en Dokploy, agrega las siguientes variables de entorno:

- `SECRET_KEY`: Clave secreta de Django (genera una nueva para producción)
- `DEBUG`: `False` para producción
- `ALLOWED_HOSTS`: Dominios permitidos separados por comas (ej: `tu-dominio.com,www.tu-dominio.com`)
- `DB_NAME`: Nombre de la base de datos (si usas PostgreSQL)
- `DB_USER`: Usuario de la base de datos
- `DB_PASSWORD`: Contraseña de la base de datos
- `DB_HOST`: Host de la base de datos
- `DB_PORT`: Puerto de la base de datos (default: 5432)

### Pasos para Deploy en Dokploy

1. **Conecta tu repositorio Git** a Dokploy (GitHub, GitLab, Bitbucket, etc.)

2. **Crea una nueva aplicación** en Dokploy y selecciona:
   
   - **Build Method**: `Nixpacks`
   - **Puerto de la aplicación**: `8000` (obligatorio)
   - Archivos: `runtime.txt` (Python 3.12), `Procfile` (comando de inicio con Gunicorn en `0.0.0.0:8000`)

3. **Configura las variables de entorno** mencionadas arriba

4. **Configura el puerto en Dokploy**: En la app → configuración, define el puerto **8000**
   - La app debe escuchar en `0.0.0.0:8000` (el `Procfile` ya lo hace)
   - Si usas otro puerto, Traefik no podrá conectarse y verás **Bad Gateway**

5. **Base de datos (opcional)**:
   - Si usas PostgreSQL, crea una base de datos en Dokploy
   - Descomenta la configuración de PostgreSQL en `sangbok_api/settings.py`
   - Agrega las variables de entorno de la base de datos

6. **Migraciones**: Se ejecutan al iniciar (definido en el `Procfile`)

7. **Habilita Auto Deploy** (opcional) para que se despliegue automáticamente cuando hagas push a tu repositorio

### Generar SECRET_KEY

Para generar una nueva SECRET_KEY, puedes ejecutar:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

O usar este comando:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Desarrollo Local

Para ejecutar localmente:

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

### Endpoints

- `/` - Health check
- `/health/` - Health check endpoint
- `/admin/` - Panel de administración de Django

### Bad Gateway al entrar a la URL

- **Puerto**: En Dokploy, la app debe tener el puerto **8000** configurado (mismo que usa Gunicorn en el `Procfile`).
- **ALLOWED_HOSTS**: Si usas dominio, añade en env `ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com` (o `*` para aceptar cualquiera).
- **Logs**: Revisa los logs del contenedor en Dokploy para ver si la app arranca o hay errores (DB, env, etc.).
