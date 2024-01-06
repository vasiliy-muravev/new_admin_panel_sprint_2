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


echo "python3 manage.py migrate"
#python3 manage.py migrate


#cat config/wsgi.py
#chown www-data:www-data config/wsgi.py

uwsgi --strict --ini /usr/src/app/uwsgi.ini
#uwsgi --strict --ini /opt/app/uwsgi.ini
#uwsgi --strict --ini uwsgi.ini



