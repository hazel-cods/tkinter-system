import sqlite3

conn = sqlite3.connect("database/school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY_KEY AUTOINCRENENT,
               user_id INTEGER,
               name TEXT NOT NULL,
               subject TEXT NOT NULL,
               section TEXT NOT NULL
               )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name TEXT,
    subject_assigned TEXT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    date TEXT,
    posted_by TEXT
)
""")

conn.commit()
conn.close()
print(" Database and Tables created succesessfully!")