import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/NFLX.csv')

print(df.shape)

# visualize
plt.figure(figsize=(16, 8))
plt.title('Netflix')
plt.xlabel('Days')
plt.ylabel('Close Price USD ($)')
plt.plot(df['Close'])
plt.show()