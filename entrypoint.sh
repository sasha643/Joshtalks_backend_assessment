#!/bin/bash

# Exit on error
set -e

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@gmail.com", "admin123")
END

# Optional: Collect static files
# python manage.py collectstatic --noinput

# Start Gunicorn server
exec gunicorn taskmanager.wsgi:application --bind 0.0.0.0:8000