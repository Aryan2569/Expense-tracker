#use of Machine learning to predict the total expenses of 7days 

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

FILE = "data/expenses.csv"

def predict_spending():
    try:
        expenses = pd.read_csv(FILE)

        if len(expenses) < 2:
            print("\n Your spending are not enough to predict your future expenses!.")             #when less data is there to predict
            return

        # creating a simple 'day count' feature (days since first entry)
        expenses["Date"] = pd.to_datetime(expenses["Date"])                                
        expenses["Day"] = (expenses["Date"] - expenses["Date"].min()).dt.days

        X = expenses[["Day"]]   
        y = expenses["Amount"]

        model = LinearRegression()
        model.fit(X, y)

        # below code will now help to predict the spending 
        future_day = pd.DataFrame([[expenses["Day"].max() + 7]], columns=["Day"])
        prediction = model.predict(future_day)

        print(f"\n Hmmm so i predict ur spending in next 7 days will be : ₹{prediction[0]:.2f}")       #prints ur nxt 7 days spending 

    except FileNotFoundError:
        print("\n No spending found.")