import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

df = pd.read_csv('./datasets/AAPL.csv')
df = df.set_index(pd.DatetimeIndex(df['Date'].values))

# visualization
plt.figure(figsize=(12.2, 4.5))
plt.plot(df['Close'], label='Close')
plt.xticks(rotation=45)
plt.title('Close price History')
plt.xlabel('Date')
plt.ylabel('Price USD')
plt.show()

# calculate the MACF and signal line indicator
# calculate the short term exponential moving average (EMA)
shortEMA = df.Close.ewm(span=12, adjust=False).mean()

# calculate the long term exponential moving average (EMA)
longEMA = df.Close.ewm(span=26, adjust=False).mean()

MACD = shortEMA - longEMA

signal = MACD.ewm(span=9, adjust=False).mean()

