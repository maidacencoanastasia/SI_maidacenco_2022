import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from imperio import BoxCoxTransformer, YeoJohnsonTransformer
from kydavra import PValueSelector

'''
Cercetarea fiecărei coloane împreună și separarat în relația cu colaona type. 
    Media. 
    Mediana.
    Moda.
    Deviația standartă.
    Variația.
    Range. 
Găsește coloanele cu cea mai mare corelație absolutp cu coloana type și încearcă sp explici de ce aceasta se întâmplă (aici poți utliza literatura despre vin).
Te rog comentează codul.
Încarcă jupyter notebook-ul pe GitHub și transmite-l mie spre verificare.
'''
df = pd.read_csv("dataset/wine-quality-white-and-red.csv")
print(df)
df.info()
# find the null values
null_v = df.isna().sum()
print(null_v) # there are no null values

print("----------------------------------")
print(df['alcohol'].value_counts())