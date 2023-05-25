from fdmanager import FDManager

# Creating object with our federalization
reader = FDManager('database_main.info')

# Creating tables,they are not exist
reader.create_table()

# These values will be written to 3 different databases with 3 different tables
values = ('Shorin', 'Joshua', 'Collins', 23, 'shorin@example.com', '789 Oak Avenue', '555-9012', 23960, 65, 25, 48, 0.6)

# Insert info to database
reader.insert_data(values)

# Select * From database
print(reader.select_data())
