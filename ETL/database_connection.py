import sqlite3


def write_from_xml(user_data, database):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Insert user data into the Users table
    cursor.execute('INSERT INTO Users (Username, Email, Password, Full_Name, Age, Address, Phone_Number) VALUES (?, '
                   '?, ?, ?, ?, ?, ?)',
                   (user_data['Username'], user_data['Email'], user_data['Password'], user_data['Full_Name'],
                    user_data['Age'], user_data['Address'], user_data['Phone_Number']))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def write_from_xslx(user_data, database_name):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Iterate over each row in the DataFrame and insert the data into the table
    for row in user_data:
        username, email, password, full_name, age, address, phone_number = row
        cursor.execute('''
            INSERT INTO Users (username, email, password, full_name, age, address, phone_number)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (username, email, password, full_name, age, address, phone_number))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def display_users_table(database_name, table_name):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Retrieve all rows from the Users table
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()

    # Display the table header
    print("Users Table:")
    print("ID | Username | Email | Password | Full Name | Age | Address | Phone Number")
    print("-" * 70)

    # Display each row of the table
    for row in rows:
        user_id, username, email, password, full_name, age, address, phone_number = row
        print(f"{user_id} | {username} | {email} | {password} | {full_name} | {age} | {address} | {phone_number}")

    # Close the connection
    conn.close()


def create_table(database_name, table_name):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    c.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            full_name TEXT,
            age INTEGER,
            address TEXT,
            phone_number TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
