import sqlite3

conn = sqlite3.connect("db.db")
print('Hello, I am ready for your requestions!')
while True:
    A = input()
    if A == '1':
        with conn:
            print(conn.execute("SELECT title FROM Books").fetchall())
    elif A == '2':
        with conn:
            print(conn.execute("SELECT name FROM Readers").fetchall())
    elif A == '3':
        B = input().split('/')
        with conn:
            conn.execute('INSERT INTO Books (author, title, publish_year) values (?, ?, ?)', (B[0], B[1], B[2]))
    elif A == '4':
        B = input()
        with conn:
            conn.execute('INSERT INTO Readers (name) values (?)', (B,))
    elif A == '5':
        B = input().split('/')
        Book = conn.execute('SELECT id FROM Books where Books.title = ?', (B[0],)).fetchone()[0]
        Reader = conn.execute('SELECT id FROM Readers where Readers.name = ?', (B[1],)).fetchone()[0]
        T = conn.execute('SELECT DATETIME(\'now\')').fetchone()[0]
        with conn:
            conn.execute('INSERT INTO Records (book_id, reader_id, taking_date, returning_date) values (?, ?, ?, ?)', (Book, Reader, T, None))
    elif A == '6':
        B = input().split('/')
        Book = conn.execute('SELECT id FROM Books where Books.title = ?', (B[0],)).fetchone()[0]
        Reader = conn.execute('SELECT id FROM Readers WHERE Readers.name = ?', (B[1],)).fetchone()[0]
        T = conn.execute('SELECT DATETIME(\'now\')').fetchone()[0]
        with conn:
            conn.execute('UPDATE Records SET returning_date = ? WHERE Records.book_id = ? AND Records.reader_id = ?', (T, Book, Reader))
