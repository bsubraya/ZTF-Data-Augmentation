%matplotlib inline
import numpy as np
from joblib import dump
import time
import os
import copy
import random
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#Scikit Gaussian Process functions
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import PairwiseKernel, RBF, Product, ConstantKernel as C, RationalQuadratic as RQ, Matern, WhiteKernel
#Scikit MultiOutput Regression class - not needed in the current version
#from sklearn.multioutput import MultiOutputRegressor
sn_lc = pd.read_csv("Users/bhagyasubrayan/Desktop/ZTF/ZTF18abbpeqo.r.txt", sep=" ",
                    header = 0, names = ['Date','Band','Magnitude','Mag_Error'])
#snlc = sn_lc[['Date','Magnitude','Mag_Error']].to_numpy()
#print(snlc)
x = sn_lc['Date'][:,np.newaxis]
y = sn_lc['Magnitude'][:,np.newaxis]
#print(x)
#print(y)
y_true_stdev = np.std(y)
kern = y_true_stdev*y_true_stdev*RQ(length_scale = 10)*RQ(length_scale = 10)
gp = GaussianProcessRegressor(kernel=kern).fit(x,y)
x_test = (sn_lc['Date'].max() - sn_lc['Date'].min()) * np.random.random_sample((1000,)) + sn_lc['Date'].min()
print(x_test)
y_mean, y_stdev = gp.predict(x_test[:,np.newaxis], return_std = True)
print(y_mean[:,0])
plt.errorbar(x, y, sn_lc['Mag_Error'][:,np.newaxis], fmt='o')
plt.gca().invert_yaxis()
plt.show()
results = np.array([x_test,y_mean[:,0]])
print(results)
plt.errorbar(results[0],results[1],y_stdev, fmt='o')
plt.gca().invert_yaxis()
plt.show()
