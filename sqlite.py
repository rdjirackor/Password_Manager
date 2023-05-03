import sqlite3
from password_generator import hashed_password,password

conn=sqlite3.connect("password_management_system.db")

#This database is where the passwords will be stored
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS GOLDEN (Password TEXT, Account TEXT,EMAIL TEXT)")


cursor.execute("INSERT INTO GOLDEN VALUES (?, ?, ?)", (hashed_password, password["Account"], password["Email"]))

cursor.execute("SELECT * FROM GOLDEN")
rows = cursor.fetchall()
for row in rows:
    print(row)


conn.commit()
conn.close()
