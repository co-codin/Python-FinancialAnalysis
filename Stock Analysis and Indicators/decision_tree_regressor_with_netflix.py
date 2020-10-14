import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
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

tree = DecisionTreeRegressor().fit(x_train, y_train)
lr = LinearRegression().fit(x_train, y_train)

x_future = df.drop(['Prediction'], 1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)

tree_prediction = tree.predict(x_future)
lr_prediction = tree.predict(x_future)

valid = df[X.shape[0]:]
valid['Predictions'] = tree_prediction
plt.figure(figsize=(16, 8))
plt.title('Model')
plt.xlabel('Days')
plt.ylabel('Close Price')
plt.plot(df['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Orrig', 'Val', 'Pred'])
plt.show()