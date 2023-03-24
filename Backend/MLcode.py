import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression

# Fetch the historical data of INFY from Yahoo Finance
def getStockData():
    infy = yf.Ticker("INFY")
    infy_history = infy.history(start="2020-01-01", end=None)

    # Create a new column for the target variable (i.e., the closing price of the stock)
    infy_history['target'] = infy_history['Close']

    # Create a new column for the feature variable (i.e., the date of the stock price)
    infy_history['date'] = pd.to_datetime(infy_history.index).astype(int)

    # Split the dataset into training and testing sets
    X_train = infy_history['date'][:500].values.reshape(-1,1)
    y_train = infy_history['target'][:500].values.reshape(-1,1)
    X_test = infy_history['date'][500:].values.reshape(-1,1)
    y_test = infy_history['target'][500:].values.reshape(-1,1)

    # Train a linear regression model on the training set
    reg = LinearRegression().fit(X_train, y_train)

    # Predict the future prices of INFY using the trained model
    future_dates = pd.date_range(start='2023-03-25', end='2024-03-24')
    future_dates = future_dates.astype(int).values.reshape(-1,1)
    future_prices = reg.predict(future_dates)

    # Print the predicted future prices
    return future_prices

