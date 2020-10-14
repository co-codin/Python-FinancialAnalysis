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

mfi = 100 * (np.array(positive_mf) / (np.array(positive_mf) + np.array(negative_mf)))

# visualization
df2 = pd.DataFrame()
df2['MFI'] = mfi

plt.figure(figsize=(12.2, 4.5))
plt.plot(df2['MFI'], label='df2')
plt.axhline(10, linestyle='--', color='orange')
plt.axhline(20, linestyle='--', color='blue')
plt.axhline(80, linestyle='--', color='blue')
plt.axhline(90, linestyle='--', color='orange')
plt.title('MFI')
plt.ylabel('MFI Values')
plt.legend(df.columns.values, loc='upper left')
plt.show()

new_df = pd.DataFrame()
new_df = df[period:]
new_df['MFI'] = mfi

# get buy and sell signals
def get_signal(data, high, low):
    buy_signal = []
    sell_signal = []

    for i in range(len(data['MFI'])):
        if data['MFI'][i] > high:
            buy_signal.append(np.nan)
            sell_signal.append(data['Close'][i])
        elif data['MFI'][i] < low:
            buy_signal.append(data['Close'][i])
            sell_signal.append(np.nan)
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)
    return  (buy_signal, sell_signal)

new_df['Buy'] = get_signal(new_df, 80, 20)[0]
new_df['Sell'] = get_signal(new_df, 80, 20)[1]


# visualizing signals
plt.figure(figsize=(12.2, 4.5))
plt.plot(new_df['Close'], label='Close Price', alpha=0.5)
plt.scatter(new_df.index, new_df['Buy'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(new_df.index, new_df['Sell'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Apple Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()