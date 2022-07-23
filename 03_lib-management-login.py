import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
from mysql.connector import Error

class LoginPage:
    def __init__(self, root=None):
        self.root = root
        self.root.title("Library Management System")
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # frame for sat application image
        self.frame_image = tk.Frame(self.main_frame)
        self.raw_image = Image.open("image/sat lms.png")     # unresize picture
        self.resized_image = ImageTk.PhotoImage(self.raw_image.resize((246,75), Image.ANTIALIAS))
        tk.Label(self.frame_image, image=self.resized_image).pack()
        self.frame_image.pack(padx=5, pady=5)

        # frame for form
        self.form_frame = tk.Frame(self.main_frame)
        self.form_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(self.form_frame, text="Database User Name : ").grid(row=0, column=0, sticky='w')
        tk.Label(self.form_frame, text="Database User Password : ").grid(row=1, column=0, sticky='w')

        self.input_user_id = tk.Entry(self.form_frame, textvariable=self.user_name, width=30)
        self.input_password = tk.Entry(self.form_frame, textvariable=self.password, show="*", width=30)
        self.input_user_id.grid(row=0, column=1)
        self.input_password.grid(row=1, column=1)

        # frame for button
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Button(self.button_frame, text="Log In", command=self.get_credential).pack(side=tk.RIGHT, padx=5)
        self.registration_label = tk.Label(self.button_frame)

    def get_credential(self):
        try : 
            mydb = mysql.connector.connect(host=HOST_NAME, user=self.user_name.get(), passwd=self.password.get(), database=DB)
            self.registration_label.config(text='Login Success', fg='green')
            self.input_user_id.delete(0,'end')
            self.input_password.delete(0,'end')
        except Error as err:
            self.registration_label.config(text='Login Failure', fg='red')
        finally :
            self.registration_label.pack(side=tk.RIGHT, padx=5)
            self.registration_label.after(1000, self.registration_label.pack_forget)
            

if __name__ == '__main__':
    HOST_NAME = "localhost"
    DB = "library"
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()