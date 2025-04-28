import mysql.connector


connection = mysql.connector.connect(user = 'root', database = 'Elite102_schema', password = 'SQL.12454933')
cursor = connection.cursor()


def view_all_data(): 
    testQuery = ("SELECT * FROM bank_database")
    cursor.execute(testQuery)
    for item in cursor:
        print(item)


def delete_all_data():
    testQuery = ("TRUNCATE TABLE bank_database")
    cursor.execute(testQuery)


def insert_account(name, account_number, pin, balance):
    testQuery = ("INSERT INTO bank_database (name, account_number, pin, balance) VALUES (%s, %s, %s, %s)")
    values = (name, account_number, pin, balance)
    cursor.execute(testQuery, values)

