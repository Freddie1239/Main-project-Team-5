import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

#Create SQL Data Base
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
""")

#Loading User info
cursor.execute("INSERT OR REPLACE INTO users VALUES (?, ?)", ("tom", "123tom"))
cursor.execute("INSERT OR REPLACE INTO users VALUES (?, ?)", ("tomsbro", "123tombro"))

conn.commit()
conn.close()

print("users.db created with users: tom / 123tom, tomsbro / 123tombro")
