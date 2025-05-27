import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Stock Portfolio
portfolio = {
    "META": 40,  # Meta Platforms (Facebook)
    "PEP": 35,  # PepsiCo
    "DIS": 25,  # Walt Disney
    "NFLX": 15,  # Netflix
    "BABA": 30,  # Alibaba Group
    "KO": 50,  # Coca-Cola
    "PFE": 60,  # Pfizer
    "INTC": 45,  # Intel
    "CSCO": 40,  # Cisco Systems
    "NKE": 20,  # Nike
}


# Set Time Interval (30 Days)
end_date = datetime.today()
start_date = end_date - timedelta(days=30)

# Fetch Data
stock_data = yf.download(
    tickers=list(portfolio.keys()),
    start=start_date,
    end=end_date,
    group_by="ticker",
    auto_adjust=True,
)

# Store holding values
holding_values = pd.DataFrame(index=stock_data.index)

# Calculate holding values
for stock in portfolio:
    if not stock_data[(stock, "Close")].isnull().all():
        holding_values[stock] = stock_data[(stock, "Close")] * portfolio[stock]

# Calculate total portfolio value (sum values accross each date)
holding_values["Total Portfolio Value"] = holding_values.sum(axis=1)

# Print latest value (Last Row)
print(f"Most Recent Value = {holding_values['Total Portfolio Value'].iloc[-1]}")

# Generate Plot
plt.figure(figsize=(14, 7))
plt.plot(
    holding_values.index,
    holding_values["Total Portfolio Value"],
    label="Total Portfolio Value",
)
plt.xlabel("Date")
plt.ylabel("Value (INR)")
plt.title("Total Portfolio Value (Last 30 Days)")
plt.legend()
plt.show()
