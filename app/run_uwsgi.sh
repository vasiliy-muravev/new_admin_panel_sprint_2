#!/usr/bin/env bash
set -e

chown www-data:www-data /var/log

# Функция для ожидания готовности базы данных
wait_for_db() {
   echo "Waiting for database..."
   while ! nc -z $DB_HOST $DB_PORT; do
     sleep 1
   done
   echo "Database is ready!"
}

 # Вызываем функцию ожидания
wait_for_db


echo "python manage.py migrate"
python manage.py migrate
python manage.py collectstatic --noinput

python ./sqlite_to_postgres/load_data.py

#python manage.py createsuperuser --noinput

uwsgi --strict --ini /usr/src/app/uwsgi.ini
