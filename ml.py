# machine learning
# import numpy as np
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

models = [
    KNeighborsRegressor(),
    DecisionTreeRegressor(),
    ExtraTreeRegressor(),
    SVR(),
    LinearRegression()
]


def test_model(df, models, target):
    X = df.drop([target], axis=1).values
    Y = df[target].values
    # impartim setul de date in doua subseturi
    # unul testare
    # al doilea antrenare
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)

    # definim dictionarul pn a calcula eroartea

    mse, mae, mse_normalized, mae_normalized = {}, {}, {}, {}
    scaler = StandardScaler()
    # antrenam setul de date pn toate modelele

    for i in range(len(models)):
        models[i].fit(X_train, Y_train)
        Y_pred = models[i].predict(X_test)

        mae[str(models[i].__class__())] = mean_absolute_error(Y_pred, Y_test)
        mse[str(models[i].__class__())] = mean_squared_error(Y_pred, Y_test)
        # transformam datele
        X_train_norm = scaler.fit_transform(X_train)
        X_test_norm = scaler.transform(X_test)

        models[i].fit(X_train_norm, Y_train)
        Y_pred = models[i].predict(X_test_norm)

        mae_normalized[str(models[i].__class__())] = mean_absolute_error(Y_pred, Y_test)
        mse_normalized[str(models[i].__class__())] = mean_squared_error(Y_pred, Y_test)

    return mse, mae, mse_normalized, mae_normalized


# read data from cv
df_init = pd.read_csv('dataset/innitial.csv')
df_selected = pd.read_csv('dataset/selected.csv')

mse, mae, mse_normalized, mae_normalized = test_model(df_init, models, 'rating_score')

print(mse, mae, mse_normalized, mae_normalized)

plt.figure(figsize=(19, 6))
plt.bar(mse.keys(), mse.values(), label='non-norm')
plt.bar(mse_normalized.keys(), mse_normalized.values(), width=0.2, label='norm')
plt.legend()
plt.show()

mse, mae, mse_normalized, mae_normalized = test_model(df_selected, models, 'rating_score')
print(mse, mae, mse_normalized, mae_normalized)

plt.figure(figsize=(19, 6))
plt.bar(mse.keys(), mse.values(), label='non-norm')
plt.bar(mse_normalized.keys(), mse_normalized.values(), width=0.2, label='norm')
plt.legend()
plt.show()

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('linear_model', LinearRegression())
])
X = df_selected.drop(['rating_score'], axis=1).values
Y = df_selected['rating_score'].values

pipe.fit(X, Y)

pickle.dump(pipe, open('pipe.pkl', 'wb'))
print(pipe['linear_model'].coef_)

coef_names = list(df_selected.iloc[:, :-1].columns)
coef_values = list(pipe['linear_model'].coef_)

plt.figure(figsize=(16, 9))
plt.bar(coef_names, coef_values)
plt.show()
