import numpy as np
import copy
import csv
from scipy.sparse import csc_matrix, save_npz, load_npz
from sklearn.linear_model import Ridge, Lasso
import os
import sys
import pandas

list1 = pandas.read_csv('')

y_predict_total = np.array(list1.ix[:,0])
y_real_total = np.array(list1.ix[:,1])

diff = np.abs(y_real_total - y_predict_total)

topIndex = np.argpartition(diff,-100)[-100:]
topIndex_sorted = topIndex[np.argsort(diff[topIndex])
#ranked by greatest differences (the most suspicious)