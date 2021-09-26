# Задание 35 (творческое)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection, datasets, linear_model, metrics
from sklearn.feature_extraction import DictVectorizer as DV
import scipy.stats as sts
import seaborn as sns


dataFrame = pd.read_csv('dataRegression.csv', sep=';')

fig, ax = plt.subplots(figsize=(14, 12))
sns.heatmap(dataFrame.corr(method='pearson'), vmax=1, vmin=-1, linewidths=0.1, annot=True, cmap='magma',
            linecolor="black", xticklabels='auto', annot_kws={'size': 12}, yticklabels='auto')

target = pd.DataFrame(dataFrame["Clicks"])
data = dataFrame[["Calls", "Sites"]]

# Разбиение набора на обучающую и тестовую выборки
train_data, test_data, train_labels, test_labels = model_selection.train_test_split(data, target, test_size=0.3)

linear_regressor = linear_model.LinearRegression()  # создание модели (регрессора)
linear_regressor.fit(train_data, train_labels)   # обучение регрессора на обучающих данных и метках
predictions = linear_regressor.predict(test_data)  # построение предсказаний на тестовых данных

# Оценка ошибки по среднему отклонению
print("Оценка ошибки по среднему отклонению", metrics.mean_absolute_error(test_labels, predictions))

# коэффициенты обученной модели
print("коэффициенты обученной модели", linear_regressor.coef_)

# свободный член обученной модели
print("свободный член обученной модели", linear_regressor.intercept_)

# Уравнение, сооветствующее обученной модели
print("y = {}*x1 + {}*x2 + {}".format(linear_regressor.coef_[0][0], linear_regressor.coef_[0][1],
                                      linear_regressor.intercept_[0]))

#  Lasso
target = pd.DataFrame(dataFrame["Clicks"])

# data = dataFrame.drop("Clicks", axis = 1)
data = dataFrame[["Calls", "Sites"]]

my_alpha = 0.5

# создание модели линейной регрессии с l1-регуляризатором
lasso_regressor = linear_model.Lasso(alpha=my_alpha, random_state=5)

lasso_regressor.fit(train_data, train_labels)    # обучение модели
lasso_predictions = lasso_regressor.predict(test_data)  # формирование массива предсказаний на тестовых данных

# Оценка ошибки по среднему отклонению
print("Оценка ошибки по среднему отклонению", metrics.mean_absolute_error(test_labels, lasso_predictions))

# коэффициенты обученной модели
print('коэффициенты обученной модели: ', lasso_regressor.coef_)

# свободный член обученной модели
print('свободный член обученной модели: ', lasso_regressor.intercept_)

# Уравнение, сооветствующее обученной модели
print("Уравнение, сооветствующее обученной модели:", "y = {}*x1 + {}*x2 + {}".format(lasso_regressor.coef_[0],
                                                                                     lasso_regressor.coef_[1],
                                                                                     lasso_regressor.intercept_))

print(f"Параметр alpha = {my_alpha}")

# Ridge
target = pd.DataFrame(dataFrame["Clicks"])

# data = dataFrame.drop("Clicks", axis = 1)
data = dataFrame[["Calls", "Sites"]]

my_alpha = 2

# создание модели линейной регрессии с l1-регуляризатором
ridge_regressor = linear_model.Ridge(alpha=my_alpha, random_state=3)
ridge_regressor.fit(train_data, train_labels)    # обучение модели
ridge_predictions = ridge_regressor.predict(test_data)  # формирование массива предсказаний на тестовых данных

# Оценка ошибки по среднему отклонению
print('Оценка ошибки по среднему отклонению: ', metrics.mean_absolute_error(test_labels, ridge_predictions))

# коэффициенты обученной модели
print('коэффициенты обученной модели: ', ridge_regressor.coef_)

# свободный член обученной модели
print('свободный член обученной модели: ', ridge_regressor.intercept_)

# Уравнение, сооветствующее обученной модели
print("Уравнение, сооветствующее обученной модели", "y = {}*x1 + {}*x2 + {}".format(ridge_regressor.coef_[0][0],
                                                                                    ridge_regressor.coef_[0][1],
                                                                                    ridge_regressor.intercept_))

# Задание на бинарное кодирование
encoder = DV(sparse=False)

data = pd.read_csv("dataRegression_1.txt", sep="\t", encoding='cp1251')

print(data.head(5))
print(data.columns)

category_column = encoder.fit_transform(data[["Region"]].T.to_dict().values())

print(category_column)

data = data.drop("Region", axis = 1)

category_binar = np.array(category_column)
print(category_binar)

data = np.concatenate((data,category_binar ), axis = 1)

np.savetxt("наше после бинарного кодирования.txt", data, delimiter = "\t")
