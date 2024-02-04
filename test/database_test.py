# flake8: noqa
import sqlite3
import os

class DataBaseTest():
    CONNECTION = os.getenv('DATABASE_PATH_TEST')

    def __init__(self) -> None:
        conn = sqlite3.connect(self.CONNECTION)
        cursor = conn.cursor()

        for db in ['students', 'books', 'loan']:
            with open(f'scripts/sql/create_table_{db}_script.sql', 'r') as file:
                cursor.executescript(file.read())

        conn.commit()
        conn.close()

    @classmethod
    def _delete_db(cls):
        conn = sqlite3.connect(cls.CONNECTION)
        cursor = conn.cursor()

        for db in ['students', 'books', 'loan']:
            cursor.execute(
                f'DELETE FROM {db};'
            )
        conn.commit()
        conn.close()
