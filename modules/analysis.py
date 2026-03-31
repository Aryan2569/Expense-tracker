import pandas as pd

FILE = "data/expenses.csv"

def show_analysis():
    try:
        expense = pd.read_csv(FILE)

        if expense.empty:
            print("\n Go Spend some money first!!.")
            return

        total = expense["Amount"].sum()
        print(f"\n Total Spending: ₹{total}")                                #will print ur total spending 

        print("\n Category-wise Spending:")
        category_sum = expense.groupby("Category")["Amount"].sum()
        print(category_sum)

        max_category = category_sum.idxmax()
        print(f"\n Highest spending category: {max_category}")               #will tell u where u spending the most

        # so this wil now check which category u are spending the most money on and then tell u about it
        print("\n Insights:")

        for category, amount in category_sum.items():
            percentage = (amount / total) * 100

            if percentage > 50:
                print(f" You are spending too much on {category} ({percentage:.1f}%)")

            elif percentage > 30:
                print(f" {category} take a good amount of money outta your pocket and it is : ({percentage:.1f}%)")

        # after getting which category u spending most it will suggest u save money blah blah blah
        print("\n Suggestion:")
        print(f"Try reducing spending on {max_category} to save more money.")

    except FileNotFoundError:   
        print("\n No expenses found.") 