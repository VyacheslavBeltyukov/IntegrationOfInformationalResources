import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table
c.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL)''')

# Commit the changes and close the connection
conn.commit()
conn.close()