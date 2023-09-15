"""Housing ML

# Data Preprocessing Tools

## Importing the libraries
"""

from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

from sklearn.metrics import mean_absolute_error

"""## Importing the dataset"""

dataset = pd.read_csv('Data2.csv')

# independen variable arays
X = dataset.iloc[:, 1:].values
# dependent variable
y = dataset.iloc[:, 0].values


imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer.fit(X[:, 0:])
X[:, 0:] = imputer.transform(X[:, 0:])


# Encoding categorical data
# Encoding the Independent Variable
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
# print(X)


"""## Splitting the dataset into the Training set and Test set"""


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)



"""## Feature Scaling"""


sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])



# Initial DecisionTreeRegressor


regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
# print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))


print("Initial Decision Tree")
print("mape!:")
print(mean_absolute_percentage_error(y_test, y_pred))


## Run grid search if you want

# from sklearn.model_selection import GridSearchCV

# parameters = {"splitter": ["best", "random"],
#               "max_depth": [1, 3, 5, 7, 9, 11, 12],
#               "min_samples_leaf": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#               "min_weight_fraction_leaf": [0.1, 0.2, 0.3, 0.4, 0.5],
#               "max_features": ["auto", "log2", "sqrt", None],
#               "max_leaf_nodes": [None, 10, 20, 30, 40, 50, 60, 70, 80, 90]}

# grid_search = GridSearchCV(regressor, param_grid=parameters, scoring='r2', cv=3, verbose=3)

# grid_search.fit(X_train, y_train)

# grid_search.best_params_

# print(grid_search.best_params_)


best_params = {'max_depth': 5,
               'max_features': None,
               'max_leaf_nodes': None,
               'min_samples_leaf': 1,
               'min_weight_fraction_leaf': 0.1,
               'splitter': 'random'}

## Tuned Regressor 
tunedRegressor = DecisionTreeRegressor(random_state=0, max_depth=1, max_features=1.0, max_leaf_nodes=None,
                                       min_samples_leaf=1, min_weight_fraction_leaf=0.1, splitter="best"

                                       )
tunedRegressor.fit(X_train, y_train)

y_pred = tunedRegressor.predict(X_test)
np.set_printoptions(precision=2)
# print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))




## XGBoost: 

regressor1 = XGBRegressor(max_depth="7")
regressor1.fit(X_train, y_train)

y_pred = regressor1.predict(X_test)
np.set_printoptions(precision=2)
# print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

print("XGboost:")
print("mape!:")
print(mean_absolute_percentage_error(y_test, y_pred))

## Random Forest Regressor:

forest = RandomForestRegressor(n_estimators=100, random_state=0)
forest.fit(X_train, y_train)
y_pred = forest.predict(X_test)


print("Random Forest Regression:")
print("mape!:")
print(mean_absolute_percentage_error(y_test, y_pred))

