import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import cross_validate
import pandas as pd

df = pd.read_csv('./datasets/breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)

print(df.head())