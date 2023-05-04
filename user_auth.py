import sqlite3 as sql
from create_account import create_user, confirm_password

user = create_user()
initially_given_password = user["Central_pass"]
confirmed_password = confirm_password(initially_given_password)

conne = sql.connect("user_details.db")

cursor = conne.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ROOT (Name TEXT, PASSWORD TEXT,EMAIL TEXT)")
cursor.execute("INSERT INTO ROOT VALUES (?, ?, ?)", (user["User"], user["Email"], confirmed_password))

cursor.execute("SELECT * FROM ROOT")
rows = cursor.fetchall()
for row in rows:
    print(row)

conne.commit()
conne.close()
