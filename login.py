import sqlite3
import hashlib
import random
import string
from tkinter import *
import re
import subprocess
    

root = Tk()
root.title("Create a new password")
root.geometry("1000x700")


name_label = Label(root, text="Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

output = Label(root, text="")
output.pack()

def login():
    namel = name_entry.get().strip()
    passwordl = password_entry.get().strip()
    conne = sqlite3.connect("user_details.db")
    cursor = conne.cursor()
    cursor.execute("SELECT * FROM USERS WHERE Name = ?", (namel,))
    row = cursor.fetchone()
    if row:
        name, email, password = row
        if passwordl == password:
            output["text"] = "User found!"
            open_file1()
    
        else:
            output["text"] = "Wrong password"
    else:
        output["text"] = "User not found"
        

create_buttonl = Button(root, text="Login", command=login)
create_buttonl.pack()
def open_file1():
    subprocess.Popen(["python", "decision.py"])
  


root.mainloop()
