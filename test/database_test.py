# flake8: noqa
import sqlite3
import os


class DataBaseTest:
    CONNECTION = os.getenv('DATABASE_PATH_TEST')

    def __init__(self) -> None:
        conn = sqlite3.connect(self.CONNECTION)
        cursor = conn.cursor()

        with open('scripts/sql/create_table_students_script.sql', 'r') as file1:
            script1 = file1.read()

        with open('scripts/sql/create_table_books_script.sql', 'r') as file2:
            script2 = file2.read()

        with open('scripts/sql/create_table_loan_script.sql', 'r') as file3:
            script3 = file3.read()

        cursor.executescript(script1)
        cursor.executescript(script2)
        cursor.executescript(script3)
        conn.commit()
        conn.close()

    def __delete_db(self):
        conn = sqlite3.connect(self.CONNECTION)
        cursor = conn.cursor()
        with open('scripts/sql/delete_all_data_students.sql', 'r') as file1:
            script1 = file1.read()

        with open('scripts/sql/delete_all_data_books.sql', 'r') as file2:
            script2 = file2.read()

        with open('scripts/sql/delete_all_data_loan.sql', 'r') as file3:
            script3 = file3.read()

        cursor.executescript(script1)
        cursor.executescript(script2)
        cursor.executescript(script3)
        conn.commit()
        conn.close()
