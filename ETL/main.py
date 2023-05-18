import openpyxl
import xml.etree.ElementTree as ElTr
import database_connection


def read_from_xml(xml_file):
    # Parse the XML file
    tree = ElTr.parse(xml_file)
    root = tree.getroot()
    user_data = {}

    # Iterate over each 'user' element in the XML
    for user_elem in root.findall('user'):
        user_data = {}
        for field in ['Username', 'Email', 'Password', 'Full_Name', 'Age', 'Address', 'Phone_Number']:
            user_data[field] = user_elem.findtext(field)

    return user_data


def read_from_xlsx(xlsx_name):
    # Read the XLSX file into a DataFrame
    workbook = openpyxl.load_workbook(xlsx_name)
    sheet = workbook.active
    dataset = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        # username, email, password, full_name, age, address, phone_number = row
        dataset.append(row)
    return dataset


if __name__ == "__main__":

    # Creating variables
    xlsxName = 'users.xlsx'
    xmlName = 'users.xml'
    dbName = 'users.db'
    dbTableName = 'Users'

    # Create table, if not exist
    database_connection.create_table(dbName, dbTableName)

    # Insert the user data into the database
    database_connection.write_from_xslx(read_from_xlsx(xlsxName), dbName)
    database_connection.write_from_xml(read_from_xml(xmlName), dbName)

    # View data in generated database
    database_connection.display_users_table(dbName, dbTableName)
