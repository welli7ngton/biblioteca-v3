CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author INTEGER,
    publishing_company TEXT,
    gender TEXT,
    amount INTEGER
)