from database import Database
from itertools import chain


# This class perform all manipulations with 3 databases, so the end user work with single database
class FDManager:
    def __init__(self, filename):
        self.database_names = []
        self.tables_names = []
        self.columns_names = []
        self.columns_select_names = []
        self.DBList = []
        # Reading information about database organization
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.database_names = [name.strip() for name in lines[0].split(',')]
            self.tables_names = [name.strip() for name in lines[1].split(',')]
            for i in range(2, 5):
                self.columns_names.append(lines[i].strip())
            for i in range(5, 8):
                self.columns_select_names.append([name.strip() for name in lines[i].split(',')])
        # Creating list of objects, each objects is individual database
        for name in self.database_names:
            self.DBList.append(Database(name))

    # Create tables in databases
    def create_table(self):
        for db, table, column in zip(self.DBList, self.tables_names, self.columns_names):
            db.create_table(table, column)

    # Insert values to every table
    def insert_data(self, values):
        data_list = [values[i:i+4] for i in range(0, len(values), 4)]
        for db, table, columns, data in zip(self.DBList, self.tables_names, self.columns_select_names, data_list):
            db.insert_data(table, columns, data)

    # Select values from every table and transform to flattened list
    def select_data(self):
        selections = []
        for db, table, columns in zip(self.DBList, self.tables_names, self.columns_select_names):
            selections.append(db.select_data(table, columns))
        flattened_list = list(chain.from_iterable(chain.from_iterable(selections)))
        return flattened_list

    # Destructor
    def __del__(self):
        for db in self.DBList:
            del db
