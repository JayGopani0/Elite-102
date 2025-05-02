import mysql.connector


connection = mysql.connector.connect(user = 'root', database = 'Elite102_schema', password = 'SQL.12454933')
cursor = connection.cursor()


def view_all_data(): 
    query = ("SELECT * FROM bank_database") # Selects all data from database 
    cursor.execute(query)
    for item in cursor:
        print(item)

# Resets the database in order to delete previous data and reset ID Auto increment
def delete_all_data():
    query = ("TRUNCATE TABLE bank_database") 
    cursor.execute(query)
    connection.commit()

# Allows the user to create an account with a name, pin and balance.
def insert_account(name, account_number, pin, balance):
    query = ("INSERT INTO bank_database (name, account_number, pin, balance) VALUES (%s, %s, %s, %s)")
    values = (name, account_number, pin, balance)
    cursor.execute(query, values)
    connection.commit()

# Allows the user to delete a specific account based on pin and account number given 
def delete_account(account_number, pin):
    query = "DELETE FROM bank_database WHERE account_number = %s AND pin = %s"
    values = (account_number, pin)
    cursor.execute(query, values)
    connection.commit()

# User can edit the name of account with proper account number and with the new name
def edit_account_name(account_number, new_name):
    cursor.execute("UPDATE bank_database SET name = %s WHERE account_number = %s", (new_name, account_number))
    connection.commit()

# User can edit the account number of account with the previous account number and with the number
def edit_account_number(account_number, new_number):
    cursor.execute("UPDATE bank_database SET account_number = %s WHERE account_number = %s", (new_number, account_number))
    connection.commit()

# User can edit the pin of account with proper account number and with the new pin number
def edit_account_pin(account_number, new_pin):
    cursor.execute("UPDATE bank_database SET pin = %s WHERE account_number = %s", (new_pin, account_number))
    connection.commit()

# Allows user to check details on the specific account given the pin and account number
def check_balance(account, pin):
    cursor.execute("SELECT balance FROM bank_database WHERE account_number = %s AND pin = %s", (account, pin))
    data = cursor.fetchone()
    print("Balance:", data[0])


# Allows user to add money into an existing account given the pin and account number
def deposit(account, pin, amount):
    cursor.execute("UPDATE bank_database SET balance = balance + %s WHERE account_number = %s AND pin = %s", (amount, account, pin))
    connection.commit()
    print("Money added successfully.")

# Allows user to withdraw money from an existing account given the pin and account number
def withdraw(account, pin, amount):
    cursor.execute("SELECT balance FROM bank_database WHERE account_number = %s AND pin = %s", (account, pin))
    data = cursor.fetchone()
    print("Money was taken out successfully.")
