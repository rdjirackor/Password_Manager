from tkinter import *
import sqlite3 as sql

root = Tk()
root.title("View Passwords")
root.geometry("1000x700")

output=Text(root)
output.pack()

def view():
    con = sql.connect("password_management_system.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM GOLDEN ")
    rows = cursor.fetchall()
    for row in rows:
        password, name, email = row
        output.insert(END, f"Password: {password}\nName: {name}\nEmail: {email}\n\n")

create_buttonl = Button(root, text="View", command=view)
create_buttonl.pack()

root.mainloop()
