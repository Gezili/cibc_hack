


import numpy as np
import copy
import csv
from scipy.sparse import csc_matrix, save_npz, load_npz
from sklearn.linear_model import Ridge, Lasso

alphas = [1e-3,1e-2,1e-1,1,1e1,1e2,1e3]
l1_errors = []
l2_errors = []

for i in range(1,2):
    X_train = load_npz('X_train_' + str(i) + '.npz')
    y_train = load_npz('y_train_' + str(i) + '.npz')
    X_test = load_npz('X_test_' + str(i) + '.npz')
    y_test = load_npz('y_test_' + str(i) + '.npz')
    for alpha in alphas:
        model = Lasso(alpha=alpha)
        y_train = y_train.toarray()
        y_test = y_test.toarray()
        model.fit(X_train, y_train)
        y_predict_half = model.predict(X_test)

        model.fit(X_test, y_test)
        y_predict = model.predict(X_train)
        
        y_predict = y_predict.extend(y_predict_half)
        print(len(y_predict))
        y_predict = np.array(y_predict)
        np.savetxt('Lasso_' + str(alpha) + '.csv', y_predict)



