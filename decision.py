from tkinter import *
import subprocess,sqlite3 as sql



def open_file1():
    subprocess.Popen(["python", "Add_a_new_password.py"])

def view_passwords():
    
        subprocess.Popen(["python", "view_pass.py"])

root = Tk()
root.title("Make a choice")
root.geometry("1000x700")

output=Label(root, text="")

name_l=Label(root,text="Account for:")
name_l.pack()
name_e=Entry(root)
name_e.pack()

email_l=Label(root,text="Email,(if there isn't, type a none)")
email_l.pack()
email_e=Entry(root)
email_e.pack()

button_add = Button(root, text="Add Password", command=open_file1)
button_add.pack()

button_display = Button(root, text="View Passwords", command=view_passwords)
button_display.pack()

root.mainloop()
