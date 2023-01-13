"""Housing ML

# Data Preprocessing Tools

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Data2.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

print(y)

# Note: used google sheets to clean up abnormal/missing data. you can use other preprocessing tools if you wish.

"""## Encoding categorical data

### Encoding the Independent Variable
"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

print(X)

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

print(X_train)

print(X_test)

print(y_train)

print(y_test)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])

print(X_train)

print(X_test)

# creating the initial decision tree regressor model

from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

from sklearn.metrics import r2_score

r2_score(y_test, y_pred)

"""Grid Search for parameter tuning"""

from sklearn.model_selection import GridSearchCV

parameters = {"splitter": ["best", "random"],
              "max_depth": [1, 3, 5, 7, 9, 11, 12],
              "min_samples_leaf": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              "min_weight_fraction_leaf": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
              "max_features": ["auto", "log2", "sqrt", None],
              "max_leaf_nodes": [None, 10, 20, 30, 40, 50, 60, 70, 80, 90]}

grid_search = GridSearchCV(regressor, param_grid=parameters, scoring='neg_mean_squared_error', cv=3, verbose=3)

grid_search.fit(X_train, y_train)

grid_search.best_params_

best_params = {'max_depth': 1,
               'max_features': 'auto',
               'max_leaf_nodes': None,
               'min_samples_leaf': 1,
               'min_weight_fraction_leaf': 0.1,
               'splitter': 'best'}

tunedRegressor = DecisionTreeRegressor(random_state=0, max_depth=1, max_features="auto", max_leaf_nodes=None,
                                       min_samples_leaf=1, min_weight_fraction_leaf=0.1, splitter="best"

                                       )
tunedRegressor.fit(X_train, y_train)

y_pred = tunedRegressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

from sklearn.metrics import r2_score

r2_score(y_test, y_pred)

"""XGBOOST"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from xgboost import XGBRegressor

regressor1 = XGBRegressor(max_depth="7")
regressor1.fit(X_train, y_train)

y_pred = regressor1.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

from sklearn.metrics import r2_score

r2_score(y_test, y_pred)


