# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:56:21 2019

@author: 138709
"""

# Random Forest Regression

# Import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1].values
X = X.reshape(-1,1)
Y = dataset.iloc[:,2].values

# Fit the Random Forest Regression Model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators = 300, random_state = 0)
model.fit(X,Y)


# Predicting the result
YPred = model.predict(6.5)


# Visualising the Random Forest Regression with higher dimensions
XGrid = np.arange(min(X), max(X), 0.01)
XGrid = XGrid.reshape((len(XGrid),1))
plt.scatter(X,Y, color = 'red')
plt.plot(XGrid, model.predict(XGrid), color = 'blue')
plt.title('Random Forest Regression')
plt.xlabel('Position')
plt.ylabel('Salaries')
plt.show()


