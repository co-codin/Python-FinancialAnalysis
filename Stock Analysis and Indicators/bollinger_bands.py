import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

df = pd.read_csv('./datasets/TSLA.csv')
df = df.set_index(pd.DatetimeIndex(df['Date'].values))

period = 20

# calculate the simple moving average (SMA)
df['SMA'] = df['Close'].rolling(window=period).mean()

# get the standard deviation
df['STD'] = df['Close'].rolling(window=period).std()

# upper boolinger band
df['Upper'] = df['SMA'] + (df['STD'] * 2)

# lower boolinger band
df['Lower'] = df['SMA'] - (df['STD'] * 2)

column_list = ['Close', 'SMA', 'Upper', 'Lower']

df[column_list].plot(figsize=(12.2, 6.4))
plt.title('Bollinger Band for Tesla')
plt.ylabel('USD Price')
plt.show()

fig = plt.figure(figsize=(12.2, 6.4))
ax = fig.add_subplot(1,1,1)
x_axis = df.index
ax.fill_between(x_axis, df['Upper'], df['Lower'], color='grey')
ax.plot(x_axis, df['Close'], color='gold', lw=3, label='Close Price')
ax.plot(x_axis, df['SMA'], color='blue', lw=3, label='Simple Moving Average')
ax.set_title('Bollinger Band for Tesla')
ax.set_xlabel('Date')
ax.set_ylabel('USD Price')
plt.xticks(rotation=45)
ax.legend()
plt.show()

new_df = df[period-1:]

def get_signal(data):
    buy_signal = []
    sell_signal = []

    for i in range(len(data['Close'])):
        if data['Close'][i] > data['Upper'][i]:
            buy_signal.append(np.nan)
            sell_signal.append(df['Close'][i])
        elif data['Close'][i] < data['Lower'][i]:
            buy_signal.append(df['Close'][i])
            sell_signal.append(np.nan)
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)
    return (buy_signal, sell_signal)

new_df['Buy'] = get_signal(new_df)[0]
new_df['Sell'] = get_signal(new_df)[1]

fig = plt.figure(figsize=(12.2, 6.4))
ax = fig.add_subplot(1,1,1)
x_axis = new_df.index
ax.fill_between(x_axis, new_df['Upper'], new_df['Lower'], color='grey')
ax.plot(x_axis, new_df['Close'], color='gold', lw=3, label='Close Price')
ax.plot(x_axis, new_df['SMA'], color='blue', lw=3, label='Simple Moving Average')
ax.scatter(x_axis, new_df['Buy'], color='green', lw=3, label='Buy', marker='^')
ax.scatter(x_axis, new_df['Sell'], color='red', lw=3, label='Buy', marker='^')
ax.set_title('Bollinger Band for Tesla')
ax.set_xlabel('Date')
ax.set_ylabel('USD Price')
plt.xticks(rotation=45)
ax.legend()
plt.show()