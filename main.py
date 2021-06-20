import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
df = pd.read_csv("dsready.csv")


cdf = df [['Number', 'Coef', 'Result']]




msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]


regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['Coef']])
train_y = np.asanyarray(train[['Result']])
regr.fit(train_x, train_y)
print('Coef:', regr.coef_)
print('Intercept:', regr.intercept_)

plt.scatter(train.Coef, train.Result, color = 'orange')
plt.plot(train_x, regr.coef_[0][0] * train_x + regr.intercept_[0], '-r')
plt.xlabel("Coef")
plt.ylabel("Result")


test_x = np.asanyarray(test[['Coef']])
test_y = np.asanyarray(test[['Result']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean(np.absolute(test_y_ - test_y) ** 2))
print("R2 score: %.2f" % r2_score(test_y_, test_y))

plt.show()




