import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

#load csv
df = pd.read_csv("Housing.csv")

Y = df['price']
X = df['lotsize']

X = X.values.reshape(len(X),1)
Y = Y.values.reshape(len(Y),1)

#split data into training/testing sets
X_train = X[:-250]
X_test = X[-250:]

#split targets into training/testing sets
Y_train = Y[:-250]
Y_test = Y[-250:]

#create linear regression object
regr = linear_model.LinearRegression()

#train the model using the training sets
regr.fit(X_train, Y_train)

#plot outputs
plt.scatter(X_test, Y_test,  color='black')
plt.title('Housing Prices in Relation to Size')
plt.xlabel('Size in sq.ft.')
plt.ylabel('Price in USD')
plt.plot(X_test, regr.predict(X_test), color='red',linewidth=3)
plt.show()