# second_file.py

import sqlite3 as sql
from create_account import create_user, confirm_password

print("second_file.py started executing")

user = create_user()
confirmed_password = confirm_password(user["Central_pass"])

conne = sql.connect("user_details.db")

cursor = conne.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ROOT (Name TEXT, PASSWORD TEXT,EMAIL TEXT)")
cursor.execute("INSERT INTO ROOT VALUES (?, ?, ?)", (user["User"], confirmed_password, user["Email"]))

cursor.execute("SELECT * FROM ROOT")
rows = cursor.fetchall()
for row in rows:
    print(row)

conne.commit()
conne.close()
