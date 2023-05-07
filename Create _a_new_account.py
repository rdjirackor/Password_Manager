from tkinter import *
import sqlite3 as sql
import re
import Add_a_new_password
import os

root = Tk()
root.geometry("1000x788")
root.title("Create an account")

name_label = Label(root, text="Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

confirm_password_label = Label(root, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = Entry(root, show="*")
confirm_password_entry.pack()

# Create Label widget to display output
output = Label(root, text="")
output.pack()

def create_account():
    # Get user inputs from Entry widgets
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    confirm_password = confirm_password_entry.get().strip()

    # Validate inputs
    if not name or not email or not password or not confirm_password:
        output["text"] = "Please fill in all fields"
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        output["text"] = "Invalid email address"
        return

    if password != confirm_password:
        output["text"] = "Passwords do not match"
        return

    # Create new user account
    conne = sql.connect("user_details.db")
    cursor = conne.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS USERS (Name TEXT, Email TEXT, Password TEXT)")
    cursor.execute("INSERT INTO USERS VALUES (?, ?, ?)", (name, email, password))
    cursor.execute("SELECT * FROM USERS")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conne.commit()
    conne.close()

    # Display success message
    output["text"] = "Account created successfully!"
    

create_button = Button(root, text="Create Account", command=create_account)
create_button.pack()

def open_file():
    root.destroy()
    os.startfile('Add_a_new_password.py')

button =Button(root, text="Add a password", command=open_file)
button.pack()

root.mainloop()
