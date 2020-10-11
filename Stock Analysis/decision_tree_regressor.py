import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv('datasets/NFLX.csv')

print(df.shape)

# visualize
# plt.figure(figsize=(16, 8))
# plt.title('Netflix')
# plt.xlabel('Days')
# plt.ylabel('Close Price USD ($)')
# plt.plot(df['Close'])
# plt.show()

df = df[['Close']]
df.head()

future_days = 25
df['Prediction'] = df[['Close']].shift(-future_days)

X = np.array(df.drop(['Prediction'], 1))[:-future_days]
y = np.array(df['Prediction'])[:-future_days]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

