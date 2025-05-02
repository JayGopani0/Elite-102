import bank_database
import random


# Creates an account using bank_database functions
def create_account(): 
    number = random.randint(10000,99999) #randomly generates an account number 
    name = input("Enter name: ")
    pin = int(input("Enter a 4-digit pin: "))
    balance = int(input("Enter the amount of money you are initially depositing: "))
    bank_database.insert_account(name, number, pin, balance) 
    print("Account successfully added.")

# Deletes an account using bank_database functions
def delete_account():
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")
    if bank_database.delete_account(account_number, pin):
        print("Account successfully deleted.")
    else:
        print("Account not found or incorrect PIN.")

# User can edit different parts of the account including name, account number and pin
def edit_account():
    print("What would you like to edit? Name, account number or pin? ")
    edit = input("N/A/P: ")
    number = int(input("Enter account number: "))
    if edit == "N":
        new_name = input("Enter new name: ")
        bank_database.edit_account_name(number, new_name)
    elif edit == "A":
        new_number = int(input("Enter new number: "))
        bank_database.edit_account_number(number, new_number)
    else:
        new_pin = int(input("Enter new pin: "))
        bank_database.edit_account_pin(number, new_pin)

# User can add, take away, or check the amount of money they have in the database
def manage_transaction():
    print("Do you want to withdraw(W), deposit(D) or check balance(B)? ")
    decision = input("W/D/B: ")
    account_number = int(input("Enter account number: "))
    pin = input("Enter your PIN: ")
    if decision == "W":
        amount = int(input("Enter the amount: "))
        bank_database.withdraw(account_number, pin, amount)
    elif decision == "D": 
        amount = int(input("Enter the amount: "))
        bank_database.deposit(account_number, pin, amount)
    else:
        bank_database.check_balance(account_number, pin)


if __name__ == "__main__":
    stay = True
    while stay:
        print("Hello and welcome to the bank!")
        print("What would you like to do today? Manage an account(A) or manage transactions(T)?: ")
        decision = input("A/T? ")
        if decision == "A":
            print("Do you want to create(C), delete(D) or edit(E) an account?")
            manage = input("C/D/E: ")
            if manage == "C":
                create_account()
            if manage == "D":
                delete_account()
            if manage == "E": 
                edit_account()
        elif decision == "T":
            manage_transaction()

        stay = input("Would you like to stay or exit? (E to exit): ")
        if stay == "E":
            break
   