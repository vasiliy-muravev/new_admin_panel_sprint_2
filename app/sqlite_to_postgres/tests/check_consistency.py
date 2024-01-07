import sqlite3
import psycopg2

dsn = {
    'dbname': 'movies_database',
    'user': 'app',
    'password': '123qwe',
    'host': 'localhost',
    'port': 5436,
    'options': '-c search_path=content',
}

# установить соединение с SQLite
sqlite_conn = sqlite3.connect('../db.sqlite')
sqlite_cursor = sqlite_conn.cursor()

# установить соединение с Postgres
pg_conn = psycopg2.connect(**dsn)
pg_cursor = pg_conn.cursor()


# film_work
# проверить количество записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT COUNT(*) FROM film_work")
pg_cursor.execute("SELECT COUNT(*) FROM film_work")
assert sqlite_cursor.fetchone()[0] == pg_cursor.fetchone()[0]

# проверить содержимое записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT * FROM film_work ORDER BY id")
pg_cursor.execute("SELECT * FROM film_work ORDER BY id")
sqlite_data = sqlite_cursor.fetchall()
pg_data = pg_cursor.fetchall()
assert sqlite_data == pg_data


#genre
# проверить количество записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT COUNT(*) FROM genre")
pg_cursor.execute("SELECT COUNT(*) FROM genre")
assert sqlite_cursor.fetchone()[0] == pg_cursor.fetchone()[0]

# проверить содержимое записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT * FROM genre ORDER BY id")
pg_cursor.execute("SELECT * FROM genre ORDER BY id")
sqlite_data = sqlite_cursor.fetchall()
pg_data = pg_cursor.fetchall()
assert sqlite_data == pg_data


# genre_film_work
# проверить количество записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT COUNT(*) FROM genre_film_work")
pg_cursor.execute("SELECT COUNT(*) FROM genre_film_work")
assert sqlite_cursor.fetchone()[0] == pg_cursor.fetchone()[0]

# проверить содержимое записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT * FROM genre_film_work ORDER BY id")
pg_cursor.execute("SELECT * FROM genre_film_work ORDER BY id")
sqlite_data = sqlite_cursor.fetchall()
pg_data = pg_cursor.fetchall()
assert sqlite_data == pg_data


# person
# проверить количество записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT COUNT(*) FROM person")
pg_cursor.execute("SELECT COUNT(*) FROM person")
assert sqlite_cursor.fetchone()[0] == pg_cursor.fetchone()[0]

# проверить содержимое записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT * FROM person ORDER BY id")
pg_cursor.execute("SELECT * FROM person ORDER BY id")
sqlite_data = sqlite_cursor.fetchall()
pg_data = pg_cursor.fetchall()
assert sqlite_data == pg_data


# person_film_work
# проверить количество записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT COUNT(*) FROM person_film_work")
pg_cursor.execute("SELECT COUNT(*) FROM person_film_work")
assert sqlite_cursor.fetchone()[0] == pg_cursor.fetchone()[0]

# проверить содержимое записей в таблице в SQLite и Postgres
sqlite_cursor.execute("SELECT * FROM person_film_work ORDER BY id")
pg_cursor.execute("SELECT * FROM person_film_work ORDER BY id")
sqlite_data = sqlite_cursor.fetchall()
pg_data = pg_cursor.fetchall()
assert sqlite_data == pg_data


# закрыть соединения
sqlite_conn.close()
pg_conn.close()