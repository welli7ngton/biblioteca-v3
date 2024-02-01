from datetime import date, timedelta
import sqlite3


class DataBase():
    DATABASE_FILE_PATH = '_library.db'
    LOAN_PERIOD = 14
    TODAY = date.today()
    DEVOLUTION_DATE = TODAY + timedelta(days=LOAN_PERIOD)

    def __init_conection(self):
        self.connection = sqlite3.connect(self.DATABASE_FILE_PATH)
        self.cursor = self.connection.cursor()

    def registerStudent(self, attributes) -> None:
        self.__init_conection()
        self.cursor.execute(
            "INSERT INTO students "
            "(name, age, contact, adress, grade_year, shift) "
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
            "adress = ?, grade_year = ?, shift = ? "
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
        book_id: int, devolution_date=None
    ) -> None:
        self.__init_conection()

        if devolution_date:
            self.cursor.execute(
                "INSERT INTO loan "
                "(student_id, book_id, loan_date, devolution_date) "
                "VALUES(?, ?, ?, ?)",
                [
                    student_id, book_id, self.TODAY,
                    (self.TODAY + timedelta(days=devolution_date))
                ]
            )
            self.connection.commit()
            self._closeConnectionAndCursor()
            return

        self.cursor.execute(
            "INSERT INTO loan "
            "(student_id, book_id, loan_date, devolution_date) "
            "VALUES(?, ?, ?, ?)",
            [
                student_id, book_id, self.TODAY, self.DEVOLUTION_DATE
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
