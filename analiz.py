import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/exported_data.csv")
print(df)
df.info()
# find the null values
null_v= df.isna().sum()
print(null_v)
# delete nul values
df = df.dropna()
# verification
null_v= df.isna().sum()
print(null_v)
