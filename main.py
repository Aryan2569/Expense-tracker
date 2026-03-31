from modules.add_expense import add_expense
from modules.view_expense import view_expenses
from modules.analysis import show_analysis
from modules.prediction import predict_spending

def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Analysis")
        print("4. Predict Spending")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_analysis()
        elif choice == "4":
            predict_spending()
        elif choice == "5":
            break
        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    main()