
import sqlite3 as db
conn=db.connect('facedb.db')
print("Database Connected")
conn.execute('''CREATE TABLE PEOPLE
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT,
       GENDER        TEXT,
       CRIMINAL         TEXT)''')
print("Table created successfully")
conn.close()
