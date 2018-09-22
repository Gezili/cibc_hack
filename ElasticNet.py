import numpy as np
# from sklearn.model_selection import train_test_split
# X = []
# y = []
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.20)

from skleran.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
alpha = [1e-3,1e-2,1e-1,1,1e1,1e2,1e3]
l1_ratio = [0,0.25,0.5,0.75,1]
regr = ElasticNet(alpha = alpha, l1_ratio = l1_ratio,max_iter = 1000)
regr.fit(X_train,y_train)
y_predict = regr.predict(X_test)
