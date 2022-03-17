import numpy as np
import seaborn as sns
from imperio import BoxCoxTransformer, YeoJohnsonTransformer
from kydavra import PValueSelector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle

df = pd.read_csv("dataset/heart.csv")
dfn = pd.read_csv("dataset/heart_numeric.csv")
print(df)
df.info()

print(dfn)
dfn.info()
# find the null values
null_v = df.isna().sum()
print(null_v) # there are no null values

print("----------------------------------")
#print(df['Age'].value_counts())
#
# plt.hist(df['Age'])
# plt.show()
# plt.hist(df['Sex'])
# plt.show()
# plt.hist(df['ChestPainType'])
# plt.show()
# plt.hist(df['Cholesterol'])
# plt.show()
# plt.hist(df['MaxHR'])
# plt.show()
# plt.hist(df['FastingBS'])
# plt.show()

from sklearn.model_selection import train_test_split
'''
Dataset: Heart Failure Prediction Dataset
Link: https://www.kaggle.com/fedesoriano/heart-failure-prediction

In this task you are going to train a bunch of Machine Learning models and try to find the one with the one with the highest accuracy.

In this task you must do the following:
Load the data set.
Split the data into train and test subset.
Create a list of the following models.
KNN
Decision Tree Classifier.
Random Forest.
Logistic Regression.
Naive Bayes.
Train each model on the train subset.
Make predictions on the test subset with each model.
Get the accuracy of each model.
Choose the best model.
Make a conclusion based on the data frame that you got.


'''
# Specify the data
p_value= PValueSelector()
sellected_cols= p_value.select(dfn, 'ST_Slope')
print(sellected_cols)
'''
['Age', 'Sex', 'ChestPainType', 'Cholesterol', 'MaxHR', 'ExerciseAngina', 'ST_Slope'] - значимые колонки
'''
