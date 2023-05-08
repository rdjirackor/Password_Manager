import sqlite3
import hashlib
import random
import string
from tkinter import *
import re

def password_generator():
  #account_name=str(input("Enter the account name, like oh, facebook:",))
  #email=str(input("Enter the email account if its associated with one, if not the enter 'none':",))
  upper_letters = string.ascii_uppercase
  lower_letters = string.ascii_lowercase
  digits = string.digits
  symbols = string.punctuation
  char = upper_letters + lower_letters + digits + symbols
  while True:
    a_random_string = ''.join(random.choices(char, k=20))
    if (sum(c.isupper() for c in a_random_string) >= 4 
        and sum(c.islower() for c in a_random_string) >= 3 
        and sum(c.isdigit() for c in a_random_string) >= 5
        and sum(c in symbols for c in a_random_string) >= 6):
      break
  return a_random_string
#The piece oof code directly, above is the returned normal password to be hashed below


with open("passwords.txt", "a") as file:
    file.write(str(password_generator()))

#print(password["Password"])
#Below is the hashing process, this will be imported in the sqlite.py file, which is the database management stuff.
#hashed_password=hashlib.sha256(password_generator().encode()).hexdigest()






'''def update_password(service_name, number_of_chars):
  new_password = password_generator(number_of_chars)
  password_dict[service_name] = new_password
  print(f"Password for {service_name} has been updated to: {new_password}")'''


root=Tk()
root.title("Create a new password")
root.geometry("1000x700")
account_label = Label(root, text="The Account for, i.e, Facebook:")
account_label.pack()
account_entry = Entry(root)
account_entry.pack()

email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

output = Label(root, text="")
output.pack()

def create_new_entry():
    account=account_entry.get().strip()
    email=email_entry.get().strip()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        output["text"] = "Invalid email address"
        return
    conn=sqlite3.connect("password_management_system.db")

#This database is where the passwords will be stored
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS GOLDEN (Password TEXT, Account TEXT,EMAIL TEXT)")


    cursor.execute("INSERT INTO GOLDEN VALUES (?, ?, ?)", (password_generator(), account,email))

    cursor.execute("SELECT * FROM GOLDEN")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    conn.commit()
    conn.close()
    output["text"] = "  Password added successfully!"

create_button = Button(root, text="Add password", command=create_new_entry)
create_button.pack()

root.mainloop()



#password_dict = {}
#This should only create a password and not bother about where it's for


#The very Important function below, generates a 24 characyter strong password
#On a second thought, I have decdide to include some parameters into the password_gen, like website or app or whatever's name and probably the email








