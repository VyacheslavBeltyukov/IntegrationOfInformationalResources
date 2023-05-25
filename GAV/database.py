import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # Create table in db
    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    # Insert data into table
    def insert_data(self, table_name, columns, values):
        query = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({','.join(['?' for _ in values])})"
        self.cursor.execute(query, values)
        self.conn.commit()

    # Insert data from table, select with specific columns
    def select_data(self, table_name, columns=None):
        if columns is None:
            query = f"SELECT * FROM {table_name}"
        else:
            query = f"SELECT {','.join(columns)} FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # Destructor
    def __del__(self):
        self.cursor.close()
        self.conn.close()
