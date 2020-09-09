import sqlite3

con = sqlite3.connect("CRUD.db")
print("Database opened successfully")

con.execute("create table CRUD_for_user_info (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, LOCATION TEXT NOT NULL, EMAIL_ID TEXT NOT NULL)")

print("Table created successfully")

con.close()
