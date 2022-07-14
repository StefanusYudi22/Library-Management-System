DROP DATABASE library;
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
    registration_date DATE,
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
    user_first_name VARCHAR(20),
    user_last_name VARCHAR(20),
    book_title VARCHAR(100),
    loan_date DATE,    # will be filled with default date of loan_function called
    supposed_return_date DATE,    # will be filled with loan_duration_function
    returned ENUM('YES','NOT YET'),    # will be filled with return_function
    returned_date DATE,    # will be filled with default date of return_function called
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
# procedure seach_book ==> procedure to show data about certain book

# procedure loan_book ==> procedure to fill table loan
# procedure return_book ==> procedure to update table loan
# procedure exit_user ==> procedure to update table user, delete user