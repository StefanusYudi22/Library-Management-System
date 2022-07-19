CREATE DATABASE IF NOT EXISTS library;
USE library;

# Table to store user info
CREATE TABLE IF NOT EXISTS lib_user(
	id_user INT AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    date_of_birth DATE,
    occupation VARCHAR(30),
    domicile VARCHAR(30),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_user PRIMARY KEY (id_user)
);

# Table to store book info
CREATE TABLE IF NOT EXISTS book(
	id_book INT AUTO_INCREMENT NOT NULL,
    title VARCHAR(100) NOT NULL,
    year_published YEAR,
    pages INT NOT NULL,
    _language ENUM('Bahasa','English','Deutch','Japan'),
    author VARCHAR(40),
	category ENUM('novel','comic','dictionary','scientific','biography','encyclopedia','thesis','magazine','history'),
    stock INT NOT NULL,
    CONSTRAINT pk_book PRIMARY KEY (id_book)               
)AUTO_INCREMENT=1000;

# Table to store loan info
CREATE TABLE IF NOT EXISTS loan(
	id_user INT, 
    id_book INT,
    user_name VARCHAR(20),
    book_title VARCHAR(100),
    loan_date DATE,    # will be filled with default date of loan_function called
    supposed_return_date DATE,    # will be filled with loan_duration_function
    returned ENUM('YES','NOT YET') DEFAULT 'NOT YET',    # will be filled with return_function
    returned_date DATE DEFAULT '0000-00-00',    # will be filled with default date of return_function called
    CONSTRAINT pk_loan PRIMARY KEY (id_user, id_book),
    CONSTRAINT fk_id_user FOREIGN KEY (id_user) REFERENCES lib_user(id_user),
	CONSTRAINT fk_id_book FOREIGN KEY (id_book) REFERENCES book(id_book)
);

# function loan_days ==> return how many days should the book borrowed
DELIMITER $$
CREATE FUNCTION loan_duration(pages INT)
RETURNS INT
DETERMINISTIC
BEGIN
	CASE
		WHEN pages < 100 THEN RETURN 3;
        WHEN pages < 300 THEN RETURN 5;
        WHEN pages < 500 THEN RETURN 7;
        ELSE RETURN 10;
	END CASE;
END $$
DELIMITER ;

# procedure show_list_user ==> procedure to get list of user
DELIMITER $$
CREATE PROCEDURE show_users()
BEGIN
	SELECT * FROM lib_user ORDER BY id_user;
END $$
DELIMITER ;

# procedure show_book ==> procedure to get list of book
DELIMITER $$
CREATE PROCEDURE show_books()
BEGIN
	SELECT * FROM book ORDER BY id_book;
END $$
DELIMITER ;

# procedure show_loan ==> procedure to get list of loan
DELIMITER $$
CREATE PROCEDURE show_loans()
BEGIN
	SELECT * FROM loan ORDER BY id_user, id_book;
END $$
DELIMITER ;

# procedure search_user ==> procedure to show data about certain user
DELIMITER $$
CREATE PROCEDURE search_user_by_name(user_name VARCHAR(20))
BEGIN
	SELECT * FROM lib_user
    WHERE first_name REGEXP user_name OR last_name REGEXP user_name;
END $$
DELIMITER ;

SELECT * FROM lib_user;
CALL search_user_by_name('tang');

# procedure seach_book ==> procedure to show data about certain book
DELIMITER $$
CREATE PROCEDURE search_book_by_title(book_title VARCHAR(100))
BEGIN
	SELECT * FROM book
    WHERE title REGEXP book_title;
END $$
DELIMITER ;

# procedure loan_book ==> procedure to fill table loan
DELIMITER $$
CREATE PROCEDURE loan_book(user_id INT, book_id INT)
BEGIN
	INSERT INTO loan (id_user, id_book, user_name, book_title, loan_date, supposed_return_date)
	WITH source_table AS(
		SELECT lb.id_user, bk.id_book, CONCAT(lb.first_name," ",lb.last_name) AS user_name, bk.title, curdate() as loan_date, DATE_ADD(curdate(), INTERVAL loan_duration(bk.pages) DAY) as supposed_returned_date
        FROM lib_user AS lb, book AS bk 
        WHERE lb.id_user = user_id AND bk.id_book = book_id
    )SELECT * FROM source_table;
END $$
DELIMITER ;

# procedure return_book ==> procedure to update table loan
DELIMITER $$
CREATE PROCEDURE return_book(user_id INT, book_id INT)
BEGIN
	UPDATE loan SET returned='YES', returned_date=curdate() WHERE id_user = user_id AND id_book = book_id;
END $$
DELIMITER ;

# procedure exit_user ==> procedure to update table user, delete user
DELIMITER $$
CREATE PROCEDURE exit_user(user_id INT)
BEGIN
	SET FOREIGN_KEY_CHECKS=0;
	IF (SELECT EXISTS (SELECT returned FROM loan WHERE id_user=user_id AND returned='NOT YET') AS isTest) = 0 THEN
		DELETE FROM lib_user WHERE id_user = user_id;
	ELSE
		SELECT 'Cannot delete user';
	END IF;
    SET FOREIGN_KEY_CHECKS=1;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE input_user(first_name VARCHAR(20), last_name VARCHAR(20), date_of_birth DATE, occupation VARCHAR(30), domicile VARCHAR(30))
BEGIN
	INSERT INTO lib_user (first_name, last_name, date_of_birth, occupation, domicile) VALUES (first_name, last_name, date_of_birth, occupation, domicile);
END $$
DELIMITER  ;

DELIMITER $$
CREATE PROCEDURE input_book(title VARCHAR(100), year_published YEAR, pages INT, _language ENUM('Bahasa','English','Deutch','Japan'), author VARCHAR(40), category ENUM('novel','comic','dictionary','scientific','biography','encyclopedia','thesis','magazine','history'), stock INT)
BEGIN
	INSERT INTO book (title, year_published, pages, _language, author, category, stock) VALUES (title, year_published, pages, _language, author, category, stock) ;
END $$
DELIMITER  ;

# Dummy data for support
INSERT INTO lib_user (first_name, last_name, date_of_birth, occupation, domicile) VALUES ('richard', 'hompton', '1996-05-16', 'office worker', 'seatle');
INSERT INTO lib_user (first_name, last_name, date_of_birth, occupation, domicile) VALUES ('stefan', 'willey', '1992-04-22', 'mine workter', 'jakarta');
INSERT INTO book (title, year_published, pages, _language, author, category, stock) VALUES ('naturo', '2022', '50', 'Japan', 'Masashi Kishimoto', 'comic', 15);
INSERT INTO book (title, year_published, pages, _language, author, category, stock) VALUES ('boruto', '2022', '50', 'Japan', 'Masashi Kishimoto', 'comic', 15);
INSERT INTO book (title, year_published, pages, _language, author, category, stock) VALUES ('one piece', '2022', '50', 'Japan', 'Oda Sensei', 'comic', 15);
INSERT INTO book (title, year_published, pages, _language, author, category, stock) VALUES ('harry potter an the order of the phoenix', '2010', '600', 'English', 'JK Rowling', 'novel', 5);

# -------------------------- (19/07/2022)
USE library;
SELECT * FROM lib_user;
SELECT * FROM book;
SELECT * FROM loan;
CALL input_book('Dunia Saham','2022',75,'Bahasa','Kompas','scientific',10);
CALL input_user('Dadang','Koswara','2002-12-05','Pedagang','Cicaheum');
CALL show_users;
CALL show_books;
DESCRIBE lib_user;