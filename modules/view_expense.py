#this  module will help in showing the expenses in main.py 

import pandas as pd

FILE = "data/expenses.csv"

def view_expenses():
    try:
        expenses = pd.read_csv(FILE)            #checks the csv file for expenses 

        if expenses.empty:
            print("\n No expenses in record...spend some money .")          
            return

        print("\n Your Expenses:\n")
        print(expenses.to_string(index=False))         #looks into the csv file and prints the expenses

    except FileNotFoundError:
        print("\n No expense file found.")          