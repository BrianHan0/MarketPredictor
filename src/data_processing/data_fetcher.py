import yfinance as yf
import os
import pandas as pd


# Fetching the data from yahoo finance
# If it already exists just read the data from it
def get_stock_data(symbol):
    filepath = "../../data/"f"{symbol}.csv"
    if (os.path.exists(filepath)):
        data = pd.read_csv(f"../../data/{symbol}.csv", index_col=0)
    else:
        data = yf.Ticker(symbol)
        data = data.history(period="max")
        data.to_csv(f"../../data/{symbol}.csv")
        # Cleaning the data
        del data["Dividends"]
        del data["Stock Splits"]
        data["Tomorrow"] = data["Close"].shift(-1)
        data["Target"] = (data["Tomorrow"] > data["Close"]).astype(int)
        # Deleting all data before 2010
        data = data.loc["2010-01-01":].copy()

    return data