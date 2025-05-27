import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 20 nifty stocks
nifty_20_stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "HINDUNILVR.NS",
    "ITC.NS",
    "LT.NS",
    "KOTAKBANK.NS",
    "SBIN.NS",
    "AXISBANK.NS",
    "ASIANPAINT.NS",
    "SUNPHARMA.NS",
    "WIPRO.NS",
    "MARUTI.NS",
    "BAJFINANCE.NS",
    "HCLTECH.NS",
    "ULTRACEMCO.NS",
    "NESTLEIND.NS",
    "TECHM.NS",
]

# Set Time Interval (30 Days)
end_date = datetime.today()
start_date = end_date - timedelta(days=30)

# Fetch Data
stock_data = yf.download(
    tickers=nifty_20_stocks,
    start=start_date,
    end=end_date,
    group_by="ticker",
    auto_adjust=True,
)

# Creare a dataframe for adj closing price
adj_close_df = pd.DataFrame(
    {stock: stock_data[(stock, "Close")] for stock in nifty_20_stocks}
)

pct_change = {}

# Calculate 1-month % change for each stock
for stock in nifty_20_stocks:
    value = adj_close_df[stock]
    pct_change[stock] = ((value.iloc[-1] - value.iloc[0]) / value.iloc[0]) * 100

# Plot Data
plot_data = {}

# Sort for losers (lowest returns)
sorted_losers = dict(sorted(pct_change.items(), key=lambda x: x[1]))

print("Top 5 Losers:")
for stock, change in list(sorted_losers.items())[:5]:
    print(f"{stock}: {change:.2f}%")
    plot_data[stock] = change

# Sort for gainers (highest returns)
sorted_gainers = dict(sorted(pct_change.items(), key=lambda x: x[1], reverse=True))

print("\nTop 5 Gainers:")
for stock, change in list(sorted_gainers.items())[:5]:
    print(f"{stock}: {change:.2f}%")
    plot_data[stock] = change

# Generate PLot
plt.figure(figsize=(14, 7))
plt.barh(plot_data.keys(), plot_data.values(), color="orange")
plt.ylabel("Stock Name")
plt.xlabel("Percentage Change (%)")
plt.title("Percentage Change Comparison Chart")
plt.show()
