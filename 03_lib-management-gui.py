import mysql_connector as mysqlcon
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Library-Management-System")

first_name = tk.StringVar()
last_name = tk.StringVar()
occupation = tk.StringVar()
domicile = tk.StringVar()
year = tk.StringVar()
month = tk.StringVar()
day = tk.StringVar()
user_id = tk.StringVar()
user_name = tk.StringVar()
book_id = tk.StringVar()
book_title = tk.StringVar()
book_pages = tk.StringVar()
book_year = tk.StringVar()
book_language = tk.StringVar()
book_author = tk.StringVar()
book_category = tk.StringVar()
book_stock = tk.StringVar()


def input_user():
    f_name = first_name.get()
    l_name = last_name.get()
    ye = year.get()
    mon = month.get()
    da = day.get()
    occ = occupation.get()
    dom = domicile.get()
    statement = f"""CALL input_user('{f_name}','{l_name}','{ye}-{mon}-{da}','{occ}','{dom}')"""
    mysqlcon.sql_execute(statement)
    
def delete_entry_lib_user():
    first_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    occupation_entry.delete(0, 'end')
    domicile_entry.delete(0, 'end')
    year_combobox.set("")
    month_combobox.set("")
    day_combobox.set("")

def input_book():
    b_title = book_title.get()
    b_pages = book_pages.get()
    b_author = book_author.get()
    b_stock = book_stock.get()
    b_year = book_year.get()
    b_lang = book_language.get()
    b_cat = book_category.get()
    statement = f"""CALL input_book('{b_title}','{b_year}',{b_pages},'{b_lang}','{b_author}','{b_cat}',{b_stock})"""
    mysqlcon.sql_execute(statement)

def delete_entry_book():
    book_title_entry.delete(0, 'end')
    book_pages_entry.delete(0, 'end')
    book_author_entry.delete(0, 'end')
    book_stock_entry.delete(0, 'end')
    book_year_combobox.set("")
    book_language_combobox.set("")
    book_category_combobox.set("")

def return_book():
    id_usr = user_id.get()
    id_bk = book_id.get()
    statement = f"""CALL return_book({id_usr},{id_bk})"""
    mysqlcon.sql_execute(statement)

def delete_return_entry():
    return_user_combobox.set("")
    return_book_combobox.set("")

def exit_user():
    id_usr = user_id.get()
    statement = f"""CALL exit_user('{id_usr}')"""
    mysqlcon.sql_execute(statement)

def loan_book():
    id_usr = user_id.get()
    id_book = book_id.get()
    statement = f"""CALL loan_book({id_usr},{id_book})"""
    mysqlcon.sql_execute(statement)

def delete_loan_book():
    loan_user_combobox.set("")
    loan_book_combobox.set("")

def delete_exit_entry():
    user_id_combobox.delete(0,'end')

def delete_search_user():
    user_name_entry.delete(0,'end')

def search_user():
    usr_name = user_name.get()
    data = mysqlcon.retrieve_table(f"search_user_by_name('{usr_name}')")
    for i in range(len(data)):
        for j in range(len(data[0])):
            box = tk.Entry(frm4)
            box.grid(row=i+2, column=j+1)
            box.insert('end',data[i][j])
            box.config(state='readonly')  

def delete_search_book():
    search_book_entry.delete(0,'end')

def search_book():
    bk_name = book_title.get()
    data = mysqlcon.retrieve_table(f"search_book_by_title('{bk_name}')")
    for i in range(len(data)):
        for j in range(len(data[0])):
            box = tk.Entry(frm8)
            box.grid(row=i+2, column=j+1)
            box.insert('end',data[i][j])
            box.config(state='readonly')  

def call_table(frame,procedure_name):
    table = mysqlcon.retrieve_table(procedure_name)     # retrieve table user from database
    for i in range(len(table)):
        for j in range(len(table[0])):
            box = tk.Entry(frame)
            box.grid(row=i, column=j+1)
            box.insert('end',table[i][j])
            box.config(state='readonly')    
    
frm1 = tk.Frame(root)
frm1.grid(row=0,column=0, sticky='news')
frm2 = tk.Frame(root)
frm2.grid(row=0,column=0, sticky='news')
frm3 = tk.Frame(root)
frm3.grid(row=0,column=0,sticky='news')
frm4 = tk.Frame(root)
frm4.grid(row=0,column=0,sticky='news')
frm5 = tk.Frame(root)
frm5.grid(row=0,column=0,sticky='news')
frm6 = tk.Frame(root)
frm6.grid(row=0,column=0,sticky='news')
frm7 = tk.Frame(root)
frm7.grid(row=0,column=0,sticky='news')
frm8 = tk.Frame(root)
frm8.grid(row=0,column=0,sticky='news')
frm9 = tk.Frame(root)
frm9.grid(row=0,column=0,sticky='news')
frm10 = tk.Frame(root)
frm10.grid(row=0,column=0,sticky='news')
frm11 = tk.Frame(root)
frm11.grid(row=0,column=0,sticky='news')
frm12 = tk.Frame(root)
frm12.grid(row=0,column=0,sticky='news')

# Main Menu
tk.Button(frm1, text="New User Registration", command=lambda:frm2.tkraise()).grid(column=0, row=0, sticky='we')
tk.Button(frm1, text="Clear User", command=lambda:frm3.tkraise()).grid(column=1, row=0, sticky='we')
tk.Button(frm1, text="Search User", command=lambda:frm4.tkraise()).grid(column=2, row=0, sticky='we')
tk.Button(frm1, text="Show List of User", command=lambda:[frm5.tkraise(),call_table(frm5,'show_users()')]).grid(column=0, row=1, sticky='we')
tk.Button(frm1, text="New Book Registration", command=lambda:frm6.tkraise()).grid(column=1, row=1, sticky='we')
tk.Button(frm1, text="Show List of Book", command=lambda:[frm7.tkraise(),call_table(frm7,'show_books()')]).grid(column=2, row=1, sticky='we')
tk.Button(frm1, text="Seach Book", command=lambda:frm8.tkraise()).grid(column=0, row=2, sticky='we')
tk.Button(frm1, text="Loan Book", command=lambda:frm9.tkraise()).grid(column=1, row=2, sticky='we')
tk.Button(frm1, text="Show List of Loan", command=lambda:[frm10.tkraise(),call_table(frm10,'show_loans()')]).grid(column=2, row=2, sticky='we')
tk.Button(frm1, text="Return Book", command=lambda:frm11.tkraise()).grid(column=0, row=3, sticky='we')
tk.Button(frm1, text="Show List of Return", command=lambda:[frm12.tkraise(),call_table(frm12,'show_returns()')]).grid(column=1, row=3, sticky='we')
tk.Button(frm1, text="Quit", command=root.destroy).grid(column=2, row=3, sticky='we')

# New User Registration
tk.Button(frm2, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)

tk.Label(frm2, text="First Name* : ").grid(column=1, row=0, sticky='w')
tk.Label(frm2, text="Last Name* : ").grid(column=1, row=1, sticky='w')
tk.Label(frm2, text="Date of Birth : ").grid(column=1, row=2, sticky='w')
tk.Label(frm2, text="Occupation : ").grid(column=1, row=3, sticky='w')
tk.Label(frm2, text="Domicile : ").grid(column=1, row=4, sticky='w')
tk.Label(frm2, text="Year : ").grid(column=2, row=2, sticky='w')
tk.Label(frm2, text="Month : ").grid(column=4, row=2, sticky='w')
tk.Label(frm2, text="Day : ").grid(column=6, row=2, sticky='w')

first_name_entry = tk.Entry(frm2, textvariable=first_name)
last_name_entry = tk.Entry(frm2, textvariable=last_name)
occupation_entry = tk.Entry(frm2, textvariable=occupation)
domicile_entry = tk.Entry(frm2, textvariable=domicile)

year_combobox = ttk.Combobox(frm2, textvariable=year, values=list(range(1990,2050)), width=4)
month_combobox = ttk.Combobox(frm2, textvariable=month, values=list(range(1,13)), width=2)
day_combobox = ttk.Combobox(frm2, textvariable=day, values=list(range(1,31)), width=2)

first_name_entry.grid(column=2, row=0, columnspan=6, sticky='we', padx=5)
last_name_entry.grid(column=2, row=1, columnspan=6, sticky='we', padx=5)
occupation_entry.grid(column=2, row=3, columnspan=6, sticky='we', padx=5)
domicile_entry.grid(column=2, row=4, columnspan=6, sticky='we', padx=5)
year_combobox.grid(column=3, row=2)
month_combobox.grid(column=5, row=2)
day_combobox.grid(column=7, row=2, padx=5)

tk.Button(frm2, text="Delete All", command=delete_entry_lib_user).grid(column=1, row=5, pady=10)
tk.Button(frm2, text="Submit", command=lambda:[input_user(),delete_entry_lib_user()]).grid(column=2, row=5, pady=10)

# Exit User
tk.Button(frm3, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)
tk.Label(frm3, text="User_id : ").grid(column=1, row=0)
user_id_combobox = ttk.Combobox(frm3, textvariable=user_id, values=list(range(1,20)))
user_id_combobox.grid(column=2, row=0)
tk.Button(frm3, text="Delete User", command=lambda:[exit_user(),delete_exit_entry()]).grid(column=1,row=1)

# Search User
tk.Button(frm4, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)
tk.Label(frm4, text="user_name : ").grid(column=1, row=0, sticky='w')
user_name_entry = ttk.Entry(frm4, textvariable=user_name)
user_name_entry.grid(column=2, row=0)
tk.Button(frm4, text="Search", command=lambda:[search_user(),delete_search_user()]).grid(column=2, row=1)
tk.Button(frm4, text="Delete", command=delete_search_user).grid(column=1, row=1)


# Show List of User
tk.Button(frm5, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)

# New Book Registration
tk.Button(frm6, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)

tk.Label(frm6, text="Title* : ").grid(column=1, row=0, sticky='w')
tk.Label(frm6, text="Year Publication : ").grid(column=1, row=1, sticky='w')
tk.Label(frm6, text="Pages : ").grid(column=1, row=2, sticky='w')
tk.Label(frm6, text="Language : ").grid(column=1, row=3, sticky='w')
tk.Label(frm6, text="Author : ").grid(column=1, row=4, sticky='w')
tk.Label(frm6, text="Category : ").grid(column=1, row=5, sticky='w')
tk.Label(frm6, text="Stock : ").grid(column=1, row=6, sticky='w')

book_title_entry = tk.Entry(frm6, textvariable=book_title)
book_pages_entry = tk.Entry(frm6, textvariable=book_pages)
book_author_entry = tk.Entry(frm6, textvariable=book_author)
book_stock_entry = tk.Entry(frm6, textvariable=book_stock)

book_year_combobox = ttk.Combobox(frm6, textvariable=book_year, values=list(range(1990,2022)), width=4)
book_language_combobox = ttk.Combobox(frm6, textvariable=book_language, values=['Bahasa','English','Deutch','Japan'], width=8)
book_category_combobox = ttk.Combobox(frm6, textvariable=book_category, values=['novel','comic','dictionary','scientific',
                         'biography','encyclopedia','thesis','magazine','history'], width=10)

book_title_entry.grid(column=2, row=0)
book_author_entry.grid(column=2, row=4)
book_stock_entry.grid(column=2, row=6)
book_pages_entry.grid(column=2, row=2)
book_year_combobox.grid(column=2, row=1, sticky='w')
book_language_combobox.grid(column=2, row=3, sticky='w')
book_category_combobox.grid(column=2, row=5, sticky='w')

tk.Button(frm6, text="Submit", command=lambda:[input_book(),delete_entry_book()]).grid(row=7, column=2, pady=5)
tk.Button(frm6, text="Delete All", command=delete_entry_book).grid(row=7, column=1, pady=5)

# Show List of Books
tk.Button(frm7, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)

# Search book 
tk.Button(frm8, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)
tk.Label(frm8, text="book_title : ").grid(column=1, row=0, sticky='w')
search_book_entry = tk.Entry(frm8, textvariable=book_title)
search_book_entry.grid(column=2, row=0, sticky='w')
tk.Button(frm8, text="Search", command=lambda:[search_book(), delete_search_book()]).grid(column=1, row=1, pady=5)
tk.Button(frm8, text="Delete", command=delete_search_book).grid(column=2, row=1, pady=5)

# Loan Book
tk.Button(frm9, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)
tk.Label(frm9, text="user_id : ").grid(column=1, row=0)
tk.Label(frm9, text="book_id : ").grid(column=1, row=1)

loan_user_combobox = ttk.Combobox(frm9, textvariable=user_id, values=mysqlcon.retrieve_id_user())
loan_book_combobox = ttk.Combobox(frm9, textvariable=book_id, values=mysqlcon.retrieve_id_book())

loan_user_combobox.grid(column=2, row=0)
loan_book_combobox.grid(column=2, row=1)

tk.Button(frm9, text="Loan", command=lambda:[loan_book(), delete_loan_book()]).grid(column=1, row=2)
tk.Button(frm9, text="Delete", command=delete_loan_book).grid(column=2, row=2)

# Show List of Loan
tk.Button(frm10, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)

# Return Book
tk.Button(frm11, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)
tk.Label(frm11, text="user_id : ").grid(column=1, row=0)
tk.Label(frm11, text="book_id : ").grid(column=1, row=1)

return_user_combobox = ttk.Combobox(frm11, textvariable=user_id, values=mysqlcon.retrieve_id_user_loan())
def callback(event):
    return_book_combobox['values'] = mysqlcon.retrieve_id_book_loan(user_id.get())
return_user_combobox.bind('<<ComboboxSelected>>', callback)
return_book_combobox = ttk.Combobox(frm11, textvariable=book_id)

return_user_combobox.grid(column=2, row=0)
return_book_combobox.grid(column=2, row=1)

tk.Button(frm11, text="Return", command=lambda:[return_book(),delete_return_entry()]).grid(column=1, row=2)
tk.Button(frm11, text="Delete", command=delete_return_entry).grid(column=2, row=2)

# Show List Of Returned
tk.Button(frm12, text="Back", command=lambda:frm1.tkraise()).grid(column=0, row=0)

frm1.tkraise()
root.mainloop()