#!/bin/ash

echo "Applu db migrations"
python manage.py migrate

exec "$@"