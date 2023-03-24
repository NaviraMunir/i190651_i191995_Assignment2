from nsepy import get_history
from datetime import date
from nsetools import Nse
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def extractandtraindata():
    # Load the historical data of INFY from NSE
    nse = Nse()
    start_date = date(2000, 1, 1)
    end_date = date.today()

    infy_data = get_history(symbol='INFY', start=start_date, end=end_date)

    # Convert the historical data to a pandas dataframe
    infy_df = pd.DataFrame(infy_history)

    header = infy_df.columns

    # Print the header
    print(header)

    # Create a new column for the target variable (i.e., the closing price of the stock)
    infy_df['target'] = infy_df['Close']

    # Create a new column for the feature variable (i.e., the date of the stock price)
    infy_df['date'] = pd.to_datetime(infy_df['date']).astype(int)

    # Split the dataset into training and testing sets
    X_train = infy_df['date'][:500].values.reshape(-1,1)
    y_train = infy_df['target'][:500].values.reshape(-1,1)
    X_test = infy_df['date'][500:].values.reshape(-1,1)
    y_test = infy_df['target'][500:].values.reshape(-1,1)

    # Train a linear regression model on the training set
    reg = LinearRegression().fit(X_train, y_train)

    # Predict the future prices of INFY using the trained model
    future_dates = pd.date_range(start='2023-03-25', end='2024-03-24')
    future_dates = future_dates.astype(int).values.reshape(-1,1)
    future_prices = reg.predict(future_dates)
    return future_prices

#create main function
def main():
    #call extractandtraindata function
    future_prices = extractandtraindata()
    #print future prices
    print(future_prices)