import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
warnings.filterwarnings('ignore')

df = pd.read_csv('./datasets/AAPL.csv')

print(df.head())