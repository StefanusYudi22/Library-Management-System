import mysql_connector as mysqlcon
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# front menu of the library management system application
class StartPage:
    def __init__(self, root=None):
        self.root = root
        self.root.title("Library Management System")
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # frame for sat application image
        self.frame_image = tk.Frame(self.main_frame)
        self.raw_image = Image.open("image/sat application.png")     # unresize picture
        self.resized_image = ImageTk.PhotoImage(self.raw_image.resize((150,75), Image.ANTIALIAS))
        tk.Label(self.frame_image, image=self.resized_image).pack()
        self.frame_image.pack(padx=5, pady=5)

        # frame for menu buttons
        self.frame_buttons = tk.Frame(self.main_frame)
        self.frame_buttons.pack(padx=10, pady=10)
        self.menu_1 = tk.Button(self.frame_buttons, text="New User Registration",
                                command=lambda:[self.main_frame.pack_forget(), self.user_registration.start_page()])
        self.menu_2 = tk.Button(self.frame_buttons, text="New Book Registration",
                                command=lambda:[self.main_frame.pack_forget(), self.book_registration.start_page()])
        self.menu_3 = tk.Button(self.frame_buttons, text="Show List of User",
                               command=lambda:[self.main_frame.pack_forget(), self.show_users.start_page()])
        self.menu_4 = tk.Button(self.frame_buttons, text="Show List of Book",
                               command=lambda:[self.main_frame.pack_forget(), self.show_books.start_page()])
        self.menu_5 = tk.Button(self.frame_buttons, text="Show List of Loan",
                               command=lambda:[self.main_frame.pack_forget(), self.show_loans.start_page()])
        self.menu_6 = tk.Button(self.frame_buttons, text="Show List of Return",
                               command=lambda:[self.main_frame.pack_forget(), self.show_returns.start_page()])
        self.menu_7 = tk.Button(self.frame_buttons, text="Search User",
                               command=lambda:[self.main_frame.pack_forget(), self.search_user.start_page()])
        self.menu_8 = tk.Button(self.frame_buttons, text="Seach Book",
                               command=lambda:[self.main_frame.pack_forget(), self.search_book.start_page()])
        self.menu_9 = tk.Button(self.frame_buttons, text="Loan Book",
                               command=lambda:[self.main_frame.pack_forget(), self.loan_book.start_page()])
        self.menu_10 = tk.Button(self.frame_buttons, text="Return Book",
                                command=lambda:[self.main_frame.pack_forget(), self.return_book.start_page()])
        self.menu_11 = tk.Button(self.frame_buttons, text="Clear User",
                                command=lambda:[self.main_frame.pack_forget(), self.delete_user.start_page()])

        self.menu_1.grid(column=0, row=0, columnspan=7, sticky='we', pady=3)
        self.menu_2.grid(column=7, row=0, columnspan=6, sticky='we', pady=3)
        self.menu_3.grid(column=0, row=1, columnspan=3, sticky='we', pady=3)
        self.menu_4.grid(column=4, row=1, columnspan=3, sticky='we', pady=3)
        self.menu_5.grid(column=7, row=1, columnspan=3, sticky='we', pady=3)
        self.menu_6.grid(column=10, row=1, columnspan=3, sticky='we', pady=3)
        self.menu_7.grid(column=0, row=2, columnspan=7, sticky='we', pady=3)
        self.menu_8.grid(column=7, row=2, columnspan=6, sticky='we', pady=3)
        self.menu_9.grid(column=0, row=3, columnspan=5, sticky='we', pady=3)
        self.menu_10.grid(column=5, row=3, columnspan=4, sticky='we', pady=3)
        self.menu_11.grid(column=9, row=3, columnspan=4, sticky='we', pady=3)
        # tk.Button(self.frame_buttons, text="Quit", command=self.root.destroy).grid(column=2, row=3, sticky='we')

        # menu frame instance
        self.user_registration = UserRegistration(master=self.root, app=self)
        self.book_registration = BookRegistration(master=self.root, app=self)
        self.show_users = Show(master=self.root, app=self, procedure="show_users")
        self.show_books = Show(master=self.root, app=self, procedure="show_books")
        self.show_loans = Show(master=self.root, app=self, procedure="show_loans")
        self.show_returns = Show(master=self.root, app=self, procedure="show_returns")
        self.search_user = Search(master=self.root, app=self, mode="user")
        self.search_book = Search(master=self.root, app=self, mode="book")
        self.loan_book = BookTransaction(master=self.root, app=self, transaction_type="loan")
        self.return_book = BookTransaction(master=self.root, app=self, transaction_type="return")
        self.delete_user = DeleteUser(master=self.root, app=self)
    
    def main_page(self):
        self.main_frame.pack()

# menu for library user registration
class UserRegistration:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.main_frame = tk.Frame(self.master)
        
        # frame for user form
        self.frame_form = tk.Frame(self.main_frame)
        self.frame_form.pack(padx=10, pady=10)
        tk.Label(self.frame_form, text="First Name * : ").grid(column=1, row=0, sticky='w')
        tk.Label(self.frame_form, text="Last Name * : ").grid(column=1, row=1, sticky='w')
        tk.Label(self.frame_form, text="Date of Birth *").grid(column=1, row=2, sticky='w')
        tk.Label(self.frame_form, text="Occupation : ").grid(column=1, row=3, sticky='w')
        tk.Label(self.frame_form, text="Domicile : ").grid(column=1, row=4, sticky='w')
        tk.Label(self.frame_form, text="Year : ").grid(column=2, row=2, sticky='we')
        tk.Label(self.frame_form, text="Month : ").grid(column=4, row=2, sticky='we')
        tk.Label(self.frame_form, text="Day : ").grid(column=6, row=2, sticky='we')
        tk.Label(self.frame_form, text="* = Required field").grid(columns=1, row=5, columnspan=6, sticky='w', pady=5)

        self.var_first_name = tk.StringVar()
        self.var_last_name = tk.StringVar()
        self.var_occupation = tk.StringVar()
        self.var_domicile = tk.StringVar()
        self.var_year = tk.StringVar()
        self.var_month = tk.StringVar()
        self.var_day = tk.StringVar()

        self.input_first_name = tk.Entry(self.frame_form, textvariable=self.var_first_name)
        self.input_last_name = tk.Entry(self.frame_form, textvariable=self.var_last_name)
        self.input_occupation = tk.Entry(self.frame_form, textvariable=self.var_occupation)
        self.input_domicile = tk.Entry(self.frame_form, textvariable=self.var_domicile)
        self.select_year = ttk.Combobox(self.frame_form, textvariable=self.var_year, values=list(range(1950,2023)), width=4)
        self.select_month = ttk.Combobox(self.frame_form, textvariable=self.var_month, values=list(range(1,13)), width=2)
        self.select_day = ttk.Combobox(self.frame_form, textvariable=self.var_day, values=list(range(1,31)), width=2)

        self.input_first_name.grid(column=2, row=0, columnspan=6, sticky='we', padx=5)
        self.input_last_name.grid(column=2, row=1, columnspan=6, sticky='we', padx=5)
        self.input_occupation.grid(column=2, row=3, columnspan=6, sticky='we', padx=5)
        self.input_domicile.grid(column=2, row=4, columnspan=6, sticky='we', padx=5)
        self.select_year.grid(column=3, row=2)
        self.select_month.grid(column=5, row=2)
        self.select_day.grid(column=7, row=2, padx=5)

        # frame for button 
        self.frame_button = tk.Frame(self.main_frame)
        self.frame_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Button(self.frame_button, text="Back", 
                  command=self.go_back).pack(side=tk.LEFT)
        tk.Button(self.frame_button, text="Clear",
                  command=self.clear_user_registration).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_button, text="Submit", 
                  command=lambda:[self.input_user()]).pack(side=tk.RIGHT)
        self.registration_label = tk.Label(self.frame_button)

    def start_page(self):
        self.main_frame.pack()

    def go_back(self):
        self.main_frame.pack_forget()
        self.app.main_page()    

    def input_user(self):
        if (self.var_first_name.get() 
            and self.var_last_name.get() 
            and self.var_year.get() 
            and self.var_month.get() 
            and self.var_day.get()):
            self.statement = f"""CALL input_user('{self.var_first_name.get()}',
                                                 '{self.var_last_name.get()}',
                                                 '{self.var_year.get()}-{self.var_month.get()}-{self.var_day.get()}',
                                                 '{self.var_occupation.get()}',
                                                 '{self.var_domicile.get()}')"""
            mysqlcon.sql_execute(self.statement)
            self.registration_label.config(text="User Registration Successfull", fg='green')
            self.clear_user_registration()
        else:
            self.registration_label.config(text="User Registration Unsuccessfull", fg='red')
        self.registration_label.pack(side=tk.RIGHT, padx=10)     # print label after registration
        self.registration_label.after(1000, self.registration_label.pack_forget)    # retain label for 1 second
    
    def clear_user_registration(self):
        self.input_first_name.delete(0, 'end')
        self.input_last_name.delete(0, 'end')
        self.input_occupation.delete(0, 'end')
        self.input_domicile.delete(0, 'end')
        self.select_year.set("")
        self.select_month.set("")
        self.select_day.set("")
        

# menu for library book registration
class BookRegistration:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.main_frame = tk.Frame(self.master)

        # frame for user form
        self.frame_form = tk.Frame(self.main_frame)
        self.frame_form.pack(padx=10, pady=10)
        tk.Label(self.frame_form, text="Title * : ").grid(column=1, row=0, sticky='w')
        tk.Label(self.frame_form, text="Year Publication * : ").grid(column=1, row=1, sticky='w')
        tk.Label(self.frame_form, text="Pages Number * : ").grid(column=1, row=2, sticky='w')
        tk.Label(self.frame_form, text="Language * : ").grid(column=1, row=3, sticky='w')
        tk.Label(self.frame_form, text="Author : ").grid(column=1, row=4, sticky='w')
        tk.Label(self.frame_form, text="Category * : ").grid(column=1, row=5, sticky='w')
        tk.Label(self.frame_form, text="Stock * : ").grid(column=1, row=6, sticky='w')
        tk.Label(self.frame_form, text="* = Required field").grid(columns=1, row=7, columnspan=2, sticky='w', pady=5)

        self.var_book_title = tk.StringVar()
        self.var_book_pages = tk.StringVar()
        self.var_book_author = tk.StringVar()
        self.var_book_stock = tk.StringVar()
        self.var_book_year = tk.StringVar()
        self.var_book_language = tk.StringVar()
        self.var_book_category = tk.StringVar()

        self.input_book_title = tk.Entry(self.frame_form, textvariable=self.var_book_title, width=40)
        self.input_book_pages = tk.Entry(self.frame_form, textvariable=self.var_book_pages, width=40)
        self.input_book_author = tk.Entry(self.frame_form, textvariable=self.var_book_author, width=40)
        self.select_book_stock = ttk.Combobox(self.frame_form, textvariable=self.var_book_stock, values=list(range(1,51)), width=2)
        self.select_book_year = ttk.Combobox(self.frame_form, textvariable=self.var_book_year, values=list(range(1990,2022)), width=4)
        self.select_book_language = ttk.Combobox(self.frame_form, textvariable=self.var_book_language,
                                                 values=['Bahasa','English','Deutch','Japan'], width=8)
        self.select_book_category = ttk.Combobox(self.frame_form, textvariable=self.var_book_category, 
                                                values=['novel','comic','dictionary','scientific',
                                                'biography','encyclopedia','thesis','magazine','history'], width=10)

        self.input_book_title.grid(column=2, row=0)
        self.input_book_author.grid(column=2, row=4)
        self.input_book_pages.grid(column=2, row=2)
        self.select_book_stock.grid(column=2, row=6, sticky='w')
        self.select_book_year.grid(column=2, row=1, sticky='w')
        self.select_book_language.grid(column=2, row=3, sticky='w')
        self.select_book_category.grid(column=2, row=5, sticky='w')

        # frame for button 
        self.frame_button = tk.Frame(self.main_frame)
        self.frame_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Button(self.frame_button, text="Back", command=self.go_back).pack(side=tk.LEFT)
        tk.Button(self.frame_button, text="Clear",
                  command=self.clear_book_registration).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_button, text="Submit",
                  command=lambda:[self.input_book()]).pack(side=tk.RIGHT)
        self.registration_label = tk.Label(self.frame_button)

    def start_page(self):
        self.main_frame.pack()

    def go_back(self):
        self.main_frame.pack_forget()
        self.app.main_page() 
    
    def input_book(self):
        try : 
            if (self.var_book_title.get() 
                and self.var_book_pages.get()
                and self.var_book_stock.get()
                and self.var_book_year.get()
                and self.var_book_language.get()
                and self.var_book_category.get()):
                self.statement = f"""CALL input_book('{self.var_book_title.get()}',
                                                    '{self.var_book_year.get()}',
                                                    {self.var_book_pages.get()},
                                                    '{self.var_book_language.get()}',
                                                    '{self.var_book_author.get()}',
                                                    '{self.var_book_category.get()}',
                                                    {self.var_book_stock.get()})"""
                mysqlcon.sql_execute(self.statement)
                self.registration_label.config(text="Book Registration Successfull", fg='green')
                self.clear_book_registration()
            else:
                self.registration_label.config(text="Book Registration Unsuccessfull", fg='red')
            self.registration_label.pack(side=tk.RIGHT, padx=10)     # print label after registration
            self.registration_label.after(1000, self.registration_label.pack_forget)    # retain label for 1 second
        except :
            self.registration_label.config(text="pages number must be number", fg='red')
            self.registration_label.pack(side=tk.RIGHT, padx=10)     # print label after registration
            self.registration_label.after(1000, self.registration_label.pack_forget)    # retain label for 1 second

    def clear_book_registration(self):
        self.input_book_title.delete(0, 'end')
        self.input_book_pages.delete(0, 'end')
        self.input_book_author.delete(0, 'end')
        self.select_book_stock.set("")
        self.select_book_year.set("")
        self.select_book_language.set("")
        self.select_book_category.set("")

# menu for showing library content
class Show:
    def __init__ (self, master=None, app=None, procedure=None):    # procedure show_users or show_books or
        self.master = master                                       # show_loans or show_users
        self.app = app                                             
        self.procedure = procedure
        self.main_frame = tk.Frame(self.master)
        #self.v = tk.Scrollbar(self.main_frame, orient='vertical')
        #self.v.pack(side=tk.RIGHT, fill=tk.Y)

        # frame for data table
        self.frame_table = tk.Frame(self.main_frame)
        self.frame_table.pack(padx=10, pady=10)

        # frame for button
        self.frame_button = tk.Frame(self.main_frame)
        self.frame_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Button(self.frame_button, text="Back", command=self.go_back).pack(side=tk.LEFT)
    
    def start_page(self):
        self.main_frame.pack()
        self.table = mysqlcon.retrieve_table(self.procedure)     # retrieve table from database
        for i in range(len(self.table)):    # data row
            for j in range(len(self.table[0])):    # data column
                if i == 0:
                    self.box = tk.Label(self.frame_table, 
                                       justify=tk.CENTER,
                                       font="Arial 10",
                                       padx=10,
                                       bd=1,
                                       bg='#ffffff',
                                       borderwidth=1,
                                       relief="solid")
                elif i != 0 and i%2 == 1:
                    self.box = tk.Label(self.frame_table, 
                                       justify=tk.CENTER,
                                       font="Arial 10",
                                       bd=1,
                                       bg='#f5f5f5')
                else:
                    self.box = tk.Label(self.frame_table, 
                                       justify=tk.CENTER,
                                       font="Arial 10",
                                       bd=1,
                                       bg='#ffffff')

                self.box.grid(row=i, column=j+1, sticky='we')
                self.box.config(text = self.table[i][j])
                #self.box.config(state='readonly')

    def go_back(self):
        self.main_frame.pack_forget()
        self.app.main_page() 

# menu for searching book and user by name
class Search:
    def __init__ (self, master, app, mode):    # mode "user" or "book"
        self.master = master
        self.app = app
        self.main_frame = tk.Frame(self.master)
        self.mode = mode

        # frame for search menu
        self.frame_search = tk.Frame(self.main_frame)
        self.frame_search.pack(padx=10, pady=10)
        self.search_label = tk.Label(self.frame_search, text="")
        self.search_label.grid(column=1, row=0, sticky='w')
        self.label()
        self.var_search = tk.StringVar()
        self.search_entry = ttk.Entry(self.frame_search, textvariable=self.var_search, width=50)
        self.search_entry.grid(column=2, row=0)

        # frame for button
        self.frame_button = tk.Frame(self.main_frame)
        self.frame_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Button(self.frame_button, text="Back", command=self.go_back).pack(side=tk.LEFT)
        tk.Button(self.frame_button, text="Clear", command=self.clear_search).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_button, text="Search", command=lambda:[self.search(),self.clear_search()]).pack(side=tk.RIGHT)
        self.registration_label = tk.Label(self.frame_button)

        # frame for search result
        self.result_frame = tk.Frame(self.main_frame)
        self.result_frame.pack(padx = 10, pady = 10)

    def start_page(self):
        self.main_frame.pack()
        self.var_search.set("   ")    # starting point for search menu
        self.search()

    def go_back(self):
        self.main_frame.pack_forget()
        self.app.main_page() 

    def label(self):
        if self.mode == "user" :
            self.search_label.config(text = "User Name : ")
        else :
            self.search_label.config(text = "Book Name : ")

    def search(self):
        try :
            if self.mode == "user" :
                self.procedure = f"search_user_by_name('{self.var_search.get()}')"
            else :
                self.procedure = f"search_book_by_title('{self.var_search.get()}')"

            self.table = mysqlcon.retrieve_table(self.procedure)     # retrieve table from database

            for widget in self.result_frame.winfo_children():
                widget.destroy()
            
            for i in range(len(self.table)):    # data row
                for j in range(len(self.table[0])):    # data column
                    if i == 0:
                        self.box = tk.Label(self.result_frame, 
                                        justify=tk.CENTER,
                                        font="Arial 10",
                                        padx=10,
                                        bd=1,
                                        bg='#ffffff',
                                        borderwidth=1,
                                        relief="solid")
                    elif i != 0 and i%2 == 1:
                        self.box = tk.Label(self.result_frame, 
                                        justify=tk.CENTER,
                                        font="Arial 10",
                                        bd=1,
                                        bg='#f5f5f5')
                    else:
                        self.box = tk.Label(self.result_frame, 
                                        justify=tk.CENTER,
                                        font="Arial 10",
                                        bd=1,
                                        bg='#ffffff')
                    self.box.grid(row=i, column=j+1, sticky='we')
                    self.box.config(text = self.table[i][j])
        except :
            self.registration_label.config(text="Search input wrong", fg='red')
            self.registration_label.pack(side=tk.RIGHT, padx=10)     # print label after registration
            self.registration_label.after(1000, self.registration_label.pack_forget)    # retain label for 1 second

    def clear_search(self):
        self.search_entry.delete(0, 'end')

class BookTransaction:
    def __init__ (self, master=None, app=None, transaction_type=None):    # transaction "loan" or "return"
        self.master = master
        self.app = app
        self.transaction_type = transaction_type
        self.main_frame = tk.Frame(self.master)

        # frame for form
        self.frame_form = tk.Frame(self.main_frame)
        self.frame_form.pack(padx=10, pady=10)
        tk.Label(self.frame_form, text="User_id * : ").grid(column=1, row=0)
        tk.Label(self.frame_form, text="Book_id * : ").grid(column=1, row=1)

        self.var_user_id = tk.StringVar()
        self.var_book_id = tk.StringVar()

        self.select_user_id = ttk.Combobox(self.frame_form, textvariable=self.var_user_id, width=40)
        self.select_book_id = ttk.Combobox(self.frame_form, textvariable=self.var_book_id, width=40)
        self.select_user_id.bind('<<ComboboxSelected>>', self.select_value_book)

        self.select_user_id.grid(column=2, row=0)
        self.select_book_id.grid(column=2, row=1)

        # frame for button
        self.frame_button = tk.Frame(self.main_frame)
        self.frame_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Button(self.frame_button, text="Back", command=self.go_back).pack(side=tk.LEFT)
        tk.Button(self.frame_button, text="Clear",
                  command=self.clear_transaction).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_button, text="Submit",
                  command=lambda:[self.transaction()]).pack(side=tk.RIGHT)
        self.registration_label = tk.Label(self.frame_button)

    def start_page(self):
        self.main_frame.pack()
        self.select_value_user()

    def go_back(self):
        self.main_frame.pack_forget()
        self.app.main_page()

    def select_value_user(self):
        if self.transaction_type == "loan":
             self.select_user_id['values'] = mysqlcon.retrieve_id_user()
        else :
             self.select_user_id['values'] = mysqlcon.retrieve_id_user_loan()

    def select_value_book(self,event):
        if self.transaction_type == "loan":
             self.select_book_id['values'] = mysqlcon.retrieve_id_book()
        else :
             self.select_book_id['values'] = mysqlcon.retrieve_id_book_loan(self.var_user_id.get())

    def clear_transaction(self):
        self.select_user_id.set("")
        self.select_book_id.set("")

    def transaction(self):
        try : 
            if self.transaction_type == "loan":
                self.registration_label.config(text="Book Loaned", fg='green')
                statement = f"CALL loan_book({self.var_user_id.get()},{self.var_book_id.get()})" 
            else:
                self.registration_label.config(text="Book Returned", fg='green')
                statement = f"CALL return_book({self.var_user_id.get()},{self.var_book_id.get()})"
        
            mysqlcon.sql_execute(statement)
            self.clear_transaction()
        except :
            self.registration_label.config(text="Wrong input search", fg='red')

        self.registration_label.pack(side=tk.RIGHT, padx=10)     # print label after registration
        self.registration_label.after(1000, self.registration_label.pack_forget)    # retain label for 1 second

class DeleteUser:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.main_frame = tk.Frame(self.master)

        # frame for form
        self.frame_form = tk.Frame(self.main_frame)
        self.frame_form.pack(padx=10, pady=10)
        tk.Label(self.frame_form, text="User_id : ").grid(column=1, row=0)
        self.var_user_id = tk.StringVar()
        self.select_user_id = ttk.Combobox(self.frame_form, textvariable=self.var_user_id, width=40)
        self.select_user_id.grid(column=2, row=0)

        # frame for button
        self.frame_button = tk.Frame(self.main_frame)
        self.frame_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Button(self.frame_button, text="Back", command=self.go_back).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_button, text="Delete User", 
                 command=self.delete_user).pack(side=tk.RIGHT, padx=5)
        self.registration_label = tk.Label(self.frame_button)

    def start_page(self):
        self.main_frame.pack()
        self.select_value_user()

    def select_value_user(self):
        self.select_user_id['values'] = mysqlcon.retrieve_id_user()

    def go_back(self):
        self.main_frame.pack_forget()
        self.app.main_page()
    
    def delete_user(self):
        try : 
            statement = f"""CALL exit_user('{self.var_user_id.get()}')"""
            mysqlcon.sql_execute(statement)
            self.clear_delete_user()
            self.registration_label.config(text="User deleted", fg='green')
        except :
            if not self.var_user_id.get():
                self.registration_label.config(text="Wrong input", fg='red')
            else :
                self.registration_label.config(text="Cannot delete user", fg='red')

        self.registration_label.pack(side=tk.RIGHT, padx=10)     # print label after registration
        self.registration_label.after(1000, self.registration_label.pack_forget)    # retain label for 1 second

    def clear_delete_user(self):
        self.select_user_id.set("")

if __name__ == '__main__':
    root = tk.Tk()
    app = StartPage(root)
    root.mainloop()