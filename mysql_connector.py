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

def retrieve_table(table_name, procedure):
    mydb = mysql.connector.connect(host=host_name, user=user_name, passwd=password, database=db)
    mycursor = mydb.cursor()
    mycursor.execute(f"DESCRIBE {table_name}")
    header_table = []
    for header in mycursor.fetchall():
        header_table.append(header[0])     # take column name fron queery describe
    mycursor.execute(f"CALL {procedure}")
    content_table = mycursor.fetchall()
    mycursor.close
    content_table.insert(0,tuple(header_table))     # insert header tuple into content list of tuple
    return content_table