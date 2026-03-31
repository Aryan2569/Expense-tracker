import pandas as pd
from datetime import datetime
import os

FILE = "data/expenses.csv"

def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (food, travel, etc): ").strip().lower()
        note = input("Enter note: ").strip()

        date = datetime.now().strftime("%Y-%m-%d")

        new_entry = pd.DataFrame([[date, amount, category, note]],
                                 columns=["Date", "Amount", "Category", "Note"])

        if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
            new_entry.to_csv(FILE, mode='a', header=False, index=False)
        else:
            new_entry.to_csv(FILE, index=False)

        print("✅ Expense added successfully!")

    except ValueError:
        print("❌ Invalid input! Please enter correct amount.")