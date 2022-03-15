from sklearn import svm
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('machine_learning/titanic.csv')

print(data)

# Предварительная работа с данными

columns_target = ['Survived']  # наша целевая колонка

columns_train = ['Pclass', 'Sex', 'Age', 'Fare']

X = data[columns_train]
Y = data[columns_target]

# Проверяем есть ли пустые ячейки в колонках

print(X['Sex'].isnull().sum())

print(X['Pclass'].isnull().sum())

X['Fare'].isnull().sum()

X['Age'].isnull().sum()

# Заполняем пустые ячейки медианным значением по возрасту


X['Age'] = X['Age'].fillna(X['Age'].mean())

X['Age'].isnull().sum()

# Заменяем male и female на 0 и 1 с помощью словаря

d = {'male': 0, 'female': 1}  # создаем словарь

X['Sex'] = X['Sex'].apply(lambda x: d[x])

X['Sex'].head()

# Разделяем нашу выборку на обучающую и тестовую


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

# Загружаем модель Support VEctor Machine для обучения

predmodel = svm.LinearSVC()

# Обучаем модель с помощью нашей обучающей выборки

predmodel.fit(X_train, Y_train)

# Предсказываем на тестовой выборке

predmodel.predict(X_test[0:10])

# Проверяем точность предсказаний

predmodel.score(X_test, Y_test)
