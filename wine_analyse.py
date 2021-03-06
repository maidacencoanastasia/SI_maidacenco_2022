import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from imperio import BoxCoxTransformer, YeoJohnsonTransformer
from kydavra import PValueSelector

df = pd.read_csv("dataset/wine-quality-white-and-red.csv")
print(df)
df.info()
# find the null values
null_v = df.isna().sum()
print(null_v) # there are no null values

print("----------------------------------")
print(df['alcohol'].value_counts())