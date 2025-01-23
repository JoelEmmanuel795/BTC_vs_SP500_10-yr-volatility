import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf 

# Fetch BTC and SP500 data from Yahoo Finance
btc = yf.download("BTC-USD", start="2013-01-01", end="2023-01-01")
sp500 = yf.download("^GSPC", start="2013-01-01", end="2023-01-01")

# Calculate daily returns
btc['Daily Return'] = btc['Close'].pct_change()
sp500['Daily Return'] = sp500['Close'].pct_change()

# Calculate rolling volatility (standard deviation) over a 30-day window
btc['Volatility'] = btc['Daily Return'].rolling(window=30).std()
sp500['Volatility'] = sp500['Daily Return'].rolling(window=30).std()

# Plot volatility
plt.figure(figsize=(14, 7))
plt.plot(btc['Volatility'], label="BTC Volatility", color='orange')
plt.plot(sp500['Volatility'], label="S&P 500 Volatility", color='blue')
plt.title("Volatility of BTC vs S&P 500 (2013-2023)", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("30-Day Rolling Volatility", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
