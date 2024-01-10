# Проектное задание: Docker-compose
## Инструкция по запуску проекта
1. Запуск через docker-compose.

В корне проекта запустить
```
docker-compose up -d --build
```
2. Добавление в hosts.

Сайт распологается по адресу http://django/admin/ , поэтому необходимо добавить его в hosts.
На Ubuntu Переходим в /etc/hosts, добавляем строчку
```
127.0.0.1       localhost django
```
На Windows c:\Windows\System32\Drivers\etc\hosts
3. Настройка БД.
 
Задаем права пользователю в Pgsql.
Зайти через портейнер (расширение для docker desktop) в контейнер с pgsql через консоль.
Либо через команду 
```
docker exec -it postgres.local bash
```
далее в консоли проверяем пользователя, создаем если нет, выдаем права
```
psql -U postgres
CREATE USER app WITH PASSWORD '123qwe';
\du
GRANT ALL PRIVILEGES ON DATABASE movies_database TO app;
```

Если при запуске есть ошибка отсутствия базы
```
CREATE DATABASE movies_database;
```
4. В контейнере django перейти в папку фреймворка app и запустить команду создания пользователя админки
```
cd app
python manage.py createsuperuser --noinput
```

5. Задание django_api

Для тестирования импортировать в постман файл из этого репозитория django_api/movies API.postman_collection.json.
В нем уже прописаны правильные пути и подставлен id, например http://django/api/v1/movies/c4ab2597-a7a1-41a9-a4ec-40a012d4010c

## Полезные команды
### Перезапуски контейнеров
```
docker-compose down && docker-compose build --no-cache && docker-compose up
docker-compose down && docker-compose up -d --build
```
### Для запуска в режиме разработки (с маппингом портов)
```
docker-compose down && docker-compose -f docker-compose.dev.yml up -d --build
```
### List dangling images. Посмотреть не привязанные к контейнерам образы
To list dangling images by adding the filter flag, -f with a value of dangling=true to the docker images
```
docker images -f dangling=true
```
### Remove Dangling Images. Удалить не привязанные к контейнерам образы
```
docker images --quiet --filter=dangling=true | xargs --no-run-if-empty docker rmi
```

## Работа с контейнером Pgsql
### Войти контейнер под root пользователем
```
docker exec -it postgres.local bash
```
### Войти базу через пользователя postgres
```
psql -U postgres
```
### Посмотреть список пользователей
```
\du
```
### Создать пользователя
```
CREATE USER app WITH PASSWORD '123qwe';
```
### Дать права пользователю к базе
```
GRANT ALL PRIVILEGES ON DATABASE movies_database TO app;
```
### Посмотреть список баз
```
\l
```
### Создать базу
```
CREATE DATABASE movies_database;
```
### Зайти в базу movies_database под суперпользователем postgres
```
psql -U postgres -d movies_database
```
### Посмотреть список таблиц
```
\dt
```
