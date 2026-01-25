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
   - **Build Method**: Dockerfile
   - **Dockerfile Path**: `Dockerfile` (o deja el default)

3. **Configura las variables de entorno** mencionadas arriba

4. **Configura el puerto**: Asegúrate de que el puerto esté configurado como `8000` en Dokploy

5. **Base de datos (opcional)**:
   - Si usas PostgreSQL, crea una base de datos en Dokploy
   - Descomenta la configuración de PostgreSQL en `sangbok_api/settings.py`
   - Agrega las variables de entorno de la base de datos

6. **Migraciones**: Dokploy puede ejecutar comandos antes del deploy. Agrega:
   ```
   python manage.py migrate --noinput
   ```

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
