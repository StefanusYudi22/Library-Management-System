import mysql.connector
from mysql.connector import Error

host_name = "localhost"
user_name = "root"
password = "kmzway87aa"
db = "library"


def sql_execute(statement):
    mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password, database=db)
    mycursor = mydb.cursor()
    mycursor.execute(statement)
    mydb.commit()
    mycursor.close()

def retrieve_table(procedure):
    mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password, database=db)
    mycursor = mydb.cursor()
    mycursor.execute(f"CALL {procedure}")
    headers = []
    for header in mycursor.description:
        headers.append(header[0])
    content_table = mycursor.fetchall()
    content_table.insert(0,tuple(headers))
    mycursor.close()
    return content_table

def retrieve_id_user():
    mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password, database=db)
    mycursor = mydb.cursor()
    mycursor.execute('SELECT id_user FROM lib_user')
    id_user = []
    for id_u in mycursor.fetchall():
        id_user.append(id_u[0])
    mycursor.close()
    return id_user

def retrieve_id_book():
    mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password, database=db)
    mycursor = mydb.cursor()
    mycursor.execute('SELECT id_book FROM book')
    id_book = []
    for id_b in mycursor.fetchall():
        id_book.append(id_b[0])
    mycursor.close()
    return id_book

def retrieve_id_user_loan():
    mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password, database=db)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT DISTINCT id_user FROM loan WHERE returned='NOT YET'")
    id_user = []
    for id_u in mycursor.fetchall():
        id_user.append(id_u[0])
    mycursor.close()
    return id_user

def retrieve_id_book_loan(id_user):
    mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password, database=db)
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT id_book FROM loan WHERE id_user={id_user} AND returned='NOT YET'")
    id_book = []
    for id_b in mycursor.fetchall():
        id_book.append(id_b[0])
    mycursor.close()
    return id_book
