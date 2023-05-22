# Schema SQL

CREATE TABLE Books(
    id INTEGER PRIMARY KEY,
    author TEXT,
  	title TEXT, 
  	publish_year INT
);
INSERT INTO Books (author, title, publish_year)
VALUES
    ('Dante', 'La Divina Commedia', 1472),
    ('St.King', '11-22-63', 2011),
    ('Sholohov','Tihiy Don', 1940),
    ('Pasternac','Dr Givago', 1957),
    ('Marquez', 'One hundred years of solitude', 1967);
CREATE TABLE Readers(
    id INTEGER PRIMARY KEY,
    name TEXT
);    
INSERT INTO Readers (name)
VALUES
    ('Alexander'),
    ('Vasily'),
    ('Grigory');
CREATE TABLE Records(
  	id INTEGER PRIMARY KEY,
  	book_id INT, 
  	reader_id INT, 
  	taking_date DATE, 
  	returning_date DATE,
  	FOREIGN KEY (book_id) REFERENCES Books (id),
  	FOREIGN KEY (reader_id) REFERENCES Readers (id)
);
INSERT INTO Records (book_id, reader_id, taking_date, returning_date)
VALUES
    (1, 2, '2020-02-04', '2020-06-08'),
    (2, 3, '2020-10-10', '2020-11-08'),
    (3, 1, '2021-01-18', NULL ),
    (4, 3, '2021-08-12', '2021-10-16'),
    (5, 1, '2022-03-13', '2022-02-28');   
    
#Query SQL

SELECT * FROM Books;
SELECT * FROM Readers;
SELECT * FROM Records;

#2.1
SELECT book_id, title
FROM Books
INNER JOIN Records
    ON Books.id = Records.book_id
    WHERE Records.taking_date IS NOT NULL AND Records.returning_date IS NULL;

#2.2
SELECT name, title
FROM Books
INNER JOIN Records 
    ON Books.id = Records.book_id
INNER JOIN Readers
	ON Records.reader_id = Readers.id;
	
#2.3
SELECT author, COUNT(id)
FROM Books
GROUP BY author
