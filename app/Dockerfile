# Укажите необходимую версию python
FROM python:3.10

# Выберите папку, в которой будут размещаться файлы проекта внутри контейнера
WORKDIR /opt/app

# Заведите необходимые переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'
ENV ALLOWED_HOSTS='django'

# Скопируйте в контейнер файлы, которые редко меняются
#COPY run_uwsgi.sh run_uwsgi.sh
COPY uwsgi/uwsgi.ini uwsgi.ini

COPY requirements.txt requirements.txt

#COPY config/wsgi.py config/wsgi.py


#COPY run_uwsgi.sh run_uwsgi.sh

# Установите зависимости

RUN apt-get update \
     && apt-get install -y netcat-openbsd gettext \
     && rm -rf /var/lib/apt/lists/* \
     && mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --no-cache-dir --upgrade pip \
     && pip install --no-cache-dir -r requirements.txt

# Скопируйте всё оставшееся. Для ускорения сборки образа эту команду стоит разместить ближе к концу файла.
COPY . .

# Укажите порт, на котором приложение будет доступно внутри Docker-сети
EXPOSE 8000

COPY run_uwsgi.sh /usr/src/app/run_uwsgi.sh
RUN chmod +x /usr/src/app/run_uwsgi.sh

COPY uwsgi/uwsgi.ini /usr/src/app/uwsgi.ini
RUN chmod +x /usr/src/app/uwsgi.ini

COPY config/wsgi.py /usr/src/app/wsgi.py
RUN chmod +x /usr/src/app/wsgi.py

ENTRYPOINT ["/usr/src/app/run_uwsgi.sh", "0.0.0.0:8000"]



RUN chmod +x run_uwsgi.sh
RUN chmod +x uwsgi.ini
#
#ENTRYPOINT ["/opt/app"]
#CMD ["run_uwsgi.sh"]


#ENTRYPOINT [ "bin.sh", "run_uwsgi.sh"]
#ENTRYPOINT ["run_uwsgi.sh" ]
#ENTRYPOINT ["/bin/bash", "run_uwsgi.sh"]
#CMD ["uwsgi", "--strict", "--ini", "uwsgi.ini"]