import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from imperio import BoxCoxTransformer, YeoJohnsonTransformer
from kydavra import PValueSelector

df = pd.read_csv("dataset/heart.csv")
print(df)
df.info()
# find the null values
null_v = df.isna().sum()
print(null_v) # there are no null values

print("----------------------------------")
#print(df['Age'].value_counts())

plt.hist(df['Age'])
plt.show()
plt.hist(df['Sex'])
plt.show()
plt.hist(df['ChestPainType'])
plt.show()
plt.hist(df['Cholesterol'])
plt.show()
plt.hist(df['MaxHR'])
plt.show()
plt.hist(df['FastingBS'])
plt.show()


