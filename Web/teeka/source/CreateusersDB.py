import sqlite3

con=sqlite3.connect('usersDB.db')
print("Connected to database")

con.execute("create table users(id INTEGER PRIMARY KEY AUTOINCREMENT, usrname TEXT NOT NULL,password TEXT NOT NULL)")
print("Table created successfully")  

# cur = con.cursor()  
con.execute("insert into users(usrname,password) values('Jack','password')")
con.commit()
print("Added user")
  
con.close()  