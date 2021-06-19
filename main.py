from tkinter import *

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
df = pd.read_csv("FuelConsumption.csv")
df.head()

cdf = df [['ENGINESIZE', 'CYLINDERS', 'CO2EMISSIONS', 'FUELCONSUMPTION_COMB']]
cdf.head(9)




msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]


regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y)
print('Coef:', regr.coef_)
print('Intercept:', regr.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color = 'blue')
plt.plot(train_x, regr.coef_[0][0] * train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")


test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean(np.absolute(test_y_ - test_y) ** 2))
print("R2 score: %.2f" % r2_score(test_y_, test_y))

plt.show()


root = Tk()

root['bg'] = '#3254a8'
root.title('Test')
root.geometry('700x600')

root.resizable(width=False, height=False)
label1 = Label(root, text="", fg="#eee", bg="#333")
label1.pack()


def show(args):
    label1.set


btn1 = Button(root, text = "Show func", width = 15, height = 5, command = show )
btn1.pack()





root.mainloop()




