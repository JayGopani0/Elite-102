import bank_database
import random


def create_account(): 
    number = random.randint(10000,99999)
    name = input("Enter name: ")
    pin = int(input("Enter a 4-digit pin: "))
    balance = int(input("Enter the amount of money you are initially depositing: "))
    bank_database.insert_account(name, number, pin, balance)
    

bank_database.delete_all_data()
create_account()
bank_database.view_all_data()