import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Set Stock Symbol (TSLA stands for TESLA)
stock_symbol = "TSLA"

# Set a time interval of 6 months
end_date = datetime.today()
start_date = end_date - timedelta(days=180)

# Fetch Data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# print(stock_data.head())

# Calculate Simple Moving Averages (SMA)
stock_data["SMA_5"] = stock_data["Close"].rolling(window=5).mean()
stock_data["SMA_20"] = stock_data["Close"].rolling(window=20).mean()

# Number Of Rows
rows = len(stock_data)

# Create empty columns
stock_data["Buy"] = False
stock_data["Sell"] = False

# Iterate through rows
for i in range(len(stock_data)):
    sma_5 = stock_data["SMA_5"].iloc[i]
    sma_20 = stock_data["SMA_20"].iloc[i]

    # Check non null values
    if pd.notnull(sma_5) and pd.notnull(sma_20):
        if sma_5 > sma_20:
            stock_data.at[stock_data.index[i], "Buy"] = True
        else:
            stock_data.at[stock_data.index[i], "Sell"] = True

buy_signals = stock_data[stock_data["Buy"] == True]
sell_signals = stock_data[stock_data["Sell"] == True]

plt.figure(figsize=(14, 7))
plt.plot(stock_data.index, stock_data["Close"], label="Close Price")
plt.plot(stock_data.index, stock_data["SMA_5"], label="5-day SMA")
plt.plot(stock_data.index, stock_data["SMA_20"], label="20-day SMA")
plt.scatter(
    buy_signals.index,
    buy_signals["Close"],
    label="Buy Signal",
    color="red",
    s=50,
)
plt.scatter(
    sell_signals.index,
    sell_signals["Close"],
    label="Sell Signal",
    color="purple",
    s=50,
)
plt.title("Stock Closing Price and SMA Crossover (Last 6 Months)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
