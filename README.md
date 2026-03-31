#  Smart Expense Tracker (AIML Project)

**Name:** Aryan Kumar  
**Registration Number:** 25BCE10794  
**Program:** B.Tech CSE (CORE)  
**University:** VIT Bhopal  

---

##  Overview

The Smart Expense Tracker is a command-line based application designed to help students track, analyze, and predict their daily expenses.

This project uses concepts from **Data Analysis and Machine Learning** to provide insights into spending habits and assist in better financial decision-making.

---

##  Problem Statement

Students often lose track of their daily expenses, leading to overspending and poor budgeting.

There is no simple tool that:
- Tracks expenses easily  
- Analyzes spending patterns  
- Predicts future expenses  

This project solves that problem using **Python and Machine Learning**.

---

##  Key Features

- Add and store daily expenses  
- View all expenses in structured format  
- Category-wise spending analysis  
- Smart insights based on spending habits  
- Predict future expenses using Linear Regression  
- Simple and interactive command-line interface  

---

##  System Working

1. User enters expense details (amount, category, note)  
2. Data is stored in a CSV file  
3. Pandas is used for analysis  
4. Machine Learning model predicts future spending  
5. System displays insights and suggestions  

---

##  Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Git & GitHub  

---

##  Installation Guide

### 1️ Install Python
Make sure Python 3.8+ is installed on your system.

---

### 2️ Install Required Libraries

```bash
pip install pandas numpy scikit-learn


## ▶ How to Run the Project

Follow these steps to run the project on your system:

### 1️ Clone the Repository

```bash
git clone https://github.com/Aryan2569/Expense-tracker.git
cd expense-tracker

##  Sample Output

Below is an example of how the application works:

==== Expense Tracker ====
1. Add Expense
2. View Expenses
3. Show Analysis
4. Predict Spending
5. Exit

Enter choice: 1
Enter amount: ₹100
Enter category (food, travel, etc): notebook
Enter note: 
✅ Expense added successfully!

==== Expense Tracker ====
1. Add Expense
2. View Expenses
3. Show Analysis
4. Predict Spending
5. Exit

Enter choice: 2

Your Expenses:

      Date  Amount Category   Note
2026-03-31   500.0     food mayuri
2026-03-31   600.0   travel sehore
2026-03-31   100.0 notebook    NaN

==== Expense Tracker ====
1. Add Expense
2. View Expenses
3. Show Analysis
4. Predict Spending
5. Exit

Enter choice: 3

Total Spending: ₹1200.0

Category-wise Spending:
food        500.0
notebook    100.0
travel      600.0

Highest spending category: travel

Insights:
food takes a good amount of your spending (41.7%)
travel takes a good amount of your spending (50.0%)

Suggestion:
Try reducing spending on travel to save more money.

==== Expense Tracker ====
1. Add Expense
2. View Expenses
3. Show Analysis
4. Predict Spending
5. Exit

Enter choice: 4

 Based on your past spending...
You might spend around ₹400.00 in the next 7 days
