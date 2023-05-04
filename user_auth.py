import sqlite3 as sql
conne=sql.connect("user_details.db")



cursor=conne.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ROOT (Name TEXT, PASSWORD TEXT,EMAIL TEXT)")
