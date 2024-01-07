import sqlite3
import logging

from contextlib import contextmanager
from dataclasses import fields, astuple

logging.basicConfig(filename="error.log", level=logging.DEBUG, filemode="w")


# Контекстный менеджер для закрытия соединения, на случай если произойдет ошибка
@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


# Получить данные из базы
def get_data(table_name, batch):
    db_path = "/opt/app/sqlite_to_postgres/db.sqlite"
    with conn_context(db_path) as conn:
        curs = conn.cursor()
        curs.execute(f"SELECT * FROM {table_name};")
        # Используем оператор yield для возврата каждой строки в качестве элемента генератора
        while True:
            rows = curs.fetchmany(batch)
            if not rows:
                break
            yield from rows


def import_lite_to_pg(table_name, data_class, cursor, batch):
    # Получаем названия столбцов
    column_names = [
        field.name for field in fields(data_class)
    ]  # ['id', 'full_name', 'created_at', 'updated_at']
    column_names_str = ",".join(column_names)  # id,full_name,created_at,updated_at
    # В зависимости от количества колонок генерируем под них %s.
    col_count = ", ".join(["%s"] * len(column_names))  # %s, %s, %s, %s

    for row in get_data(table_name, batch):
        # Обработка каждой строки
        entity = data_class(**row)
        bind_values = cursor.mogrify(f"({col_count})", astuple(entity)).decode("utf-8")

        query = (
            f"INSERT INTO {table_name} ({column_names_str}) VALUES {bind_values} "
            f" ON CONFLICT (id) DO NOTHING"
        )

        try:
            cursor.execute(query)
        except ValueError:
            logging.error(f"Такая запись уже существует {ValueError}")
