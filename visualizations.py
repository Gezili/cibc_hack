import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import itertools
import operator
import csv

# Look at discrete variables
final_claims = pd.read_csv('claims_final.csv', header=None, names=['fam id', 'fam member id', 'provider id', 'provider type', 'state', 'date', 'procedure code', 'amount'])
final_claims.boxplot(column='amount', by='state')
plt.ylabel('amount')

final_claims.boxplot(column='amount', by='provider type')
plt.ylabel('amount')

np.correlate(final_claims['amount'], final_claims['date'])

# Look at continuous variables
final_claims[20060000 <= final_claims['date']].plot.scatter('date', 'amount')