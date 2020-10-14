import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
warnings.filterwarnings('ignore')

df = pd.read_csv('./datasets/AAPL.csv')

df = df.set_index(pd.DatetimeIndex(df['Date']))

# visualisation
plt.figure(figsize=(12.2, 4.5))
plt.plot(df['Close'], label='Close Price')
plt.title('Apple Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(df.columns.values, loc='upper left')
plt.show()

typical_price = (df['Close'] + df['High'] + df['Low']) / 3

period = 14

money_flow = typical_price * df['Volume']

positive_flow = []
negative_flow = []