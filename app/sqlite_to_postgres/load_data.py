import os
import psycopg2.extras
import dataclass_models

from dotenv import load_dotenv
from import_base import import_lite_to_pg
from contextlib import closing

dotenv_path = "/opt/app/config/.env"

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

batch = int(os.environ.get("BATCH_SIZE"))

dsn = {
    "dbname": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "options": "-c search_path=content",
}

tables = {
    "film_work": dataclass_models.FilmWork,
    "person": dataclass_models.Person,
    "genre": dataclass_models.Genre,
    "genre_film_work": dataclass_models.GenreFilmWork,
    "person_film_work": dataclass_models.PersonFilmWork,
}

with closing(psycopg2.connect(**dsn)) as conn, conn.cursor(
    cursor_factory=psycopg2.extras.DictCursor
) as cursor:
    for i in tables:
        import_lite_to_pg(i, tables[i], cursor, batch)

    conn.commit()
