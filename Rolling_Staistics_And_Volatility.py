import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Set Stock Symbol
stock_symbol = "AAPL"

# Set Time Interval (4 months)
end_date = datetime.today()
start_date = end_date - timedelta(days=120)

# Fetch data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
rows = len(stock_data)

# Calculate Daily Returns
stock_data["Daily Return"] = stock_data["Close"].pct_change() * 100

# Calculate Rolling Mean and Standard Deviation (SD => Standard Deviation)
stock_data["Rolling 7 Day Average"] = (
    stock_data["Daily Return"].rolling(window=7).mean()
)
stock_data["Rolling 7 Day SD"] = stock_data["Daily Return"].rolling(window=7).std()

# Generate Plot
plt.figure(figsize=(14, 7))
plt.plot(stock_data.index, stock_data["Daily Return"], label="Daily Return")
plt.plot(
    stock_data.index, stock_data["Rolling 7 Day Average"], label="7-day Rolling Average"
)
plt.plot(stock_data.index, stock_data["Rolling 7 Day SD"], label="7-day Rolling SD")
plt.title("Rolling Statistics and Volatility Analysis (Last 4 Months)")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.legend()
plt.show()
