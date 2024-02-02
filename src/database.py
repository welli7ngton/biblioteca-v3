from datetime import date, timedelta
import os
import sqlite3


class DataBase():
    LOAN_PERIOD = 14
    TODAY = date.today()
    DEVOLUTION_DATE = TODAY + timedelta(days=LOAN_PERIOD)

    def __init__(self, env) -> None:
        if env == 'development':
            self.DATABASE_FILE_PATH = os.getenv('DATABASE_PATH')
        else:
            self.DATABASE_FILE_PATH = os.getenv('DATABASE_PATH_TEST')

    def __init_conection(self):
        self.connection = sqlite3.connect(self.DATABASE_FILE_PATH)
        self.cursor = self.connection.cursor()

    def registerStudent(self, attributes) -> None:
        self.__init_conection()
        self.cursor.execute(
            "INSERT INTO students "
            "(name, age, contact, address_, grade_year, shift) "
            "VALUES(?, ?, ?, ?, ?, ?)",
            [
                attr for attr in attributes
            ]
        )
        self.connection.commit()
        self._closeConnectionAndCursor()

    def changeRegisterStudent(self, _id: int, attributes) -> None:
        self.__init_conection()
        self.cursor.execute(
            f"UPDATE students SET "
            "name = ?, age = ?, contact = ?, "
            "address_ = ?, grade_year = ?, shift = ? "
            f"WHERE student_id = {_id}",
            [
                attr for attr in attributes
            ]
        )
        self.connection.commit()
        self._closeConnectionAndCursor

    def registerBook(self, attributes) -> None:
        self.__init_conection()
        self.cursor.execute(
            "INSERT INTO books "
            "(title, author, publishing_company, gender, amount) "
            "VALUES(?, ?, ?, ?, ?)",
            [
                attr for attr in attributes
            ]
        )
        self.connection.commit()
        self._closeConnectionAndCursor()

    def changeRegisterBook(self, _id: int, attributes) -> None:
        self.__init_conection()
        self.cursor.execute(
            f"UPDATE books SET "
            "title = ?, author = ?, publishing_company = ?, "
            "gender = ?, amount = ? "
            f"WHERE book_id = {_id}",
            [
                attr for attr in attributes
            ]
        )
        self.connection.commit()
        self._closeConnectionAndCursor()

    def registerLoan(
        self, student_id: int,
        book_id: int, devolution_date: int = 0
    ) -> None:
        self.__init_conection()

        if devolution_date != 0:
            self.cursor.execute(
                "INSERT INTO loan "
                "(student_id, book_id, devolution_date) "
                "VALUES(?, ?, ?)",
                [
                    student_id, book_id,
                    (self.TODAY + timedelta(days=devolution_date))
                ]
            )
            self.connection.commit()
            self._closeConnectionAndCursor()
            return

        self.cursor.execute(
            "INSERT INTO loan "
            "(student_id, book_id, devolution_date) "
            "VALUES(?, ?, ?)",
            [
                student_id, book_id, self.DEVOLUTION_DATE
            ]
        )
        self.connection.commit()
        self._closeConnectionAndCursor()

    def deleteRegister(self, _id: int, table: str, column: str) -> None:
        self.__init_conection()

        if self._checkIdexistence(_id, table, column):
            self.cursor.execute(
                f"DELETE FROM {table} WHERE {column}={_id}"
            )
            self.connection.commit()
            self._closeConnectionAndCursor()

    def _checkIdexistence(self, _id: int, table: str, column) -> bool:
        self.__init_conection()

        rows = self.cursor.execute(
            f"SELECT * FROM {table} WHERE {column}"
        )

        for row in rows.fetchall():
            if _id in row:
                return True
        raise Exception("ID NÃO EXISTE")

    def _getTableInfo(self, table_name: str) -> list[tuple]:
        self.__init_conection()

        tableRows = self.cursor.execute(
            f"SELECT * FROM {table_name}"
        )

        return tableRows.fetchall()

    def _closeConnectionAndCursor(self) -> None:
        self.cursor.close()
        self.connection.close()
