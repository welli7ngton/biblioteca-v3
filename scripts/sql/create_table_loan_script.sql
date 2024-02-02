CREATE TABLE IF NOT EXISTS loan (
	loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
	student_id INTEGER,
	book_id INTEGER,
	loan_date DATE DEFAULT CURRENT_DATE,
	devolution_date DATE,
	FOREIGN KEY (student_id) REFERENCES students(student_id),
	FOREIGN KEY (book_id) REFERENCES books(book_id)
)