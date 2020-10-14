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

for i in range(1, len(typical_price)):
    if typical_price[i] > typical_price[i-1]:
        positive_flow.append(money_flow[i-1])
        negative_flow.append(0)
    elif typical_price[i] < typical_price[i-1]:
        positive_flow.append(0)
        negative_flow.append(money_flow[i - 1])
    else:
        positive_flow.append(0)
        negative_flow.append(0)

positive_mf = []
negative_mf = []

for i in range(period-1, len(positive_flow)):
    positive_mf.append( sum(positive_flow[i-period+1:i+1]) )

for i in range(period-1, len(negative_flow)):
    negative_mf.append( sum(negative_flow[i-period+1:i+1]) )

# mfi = 100 * 