


import numpy as np
import copy
import csv
from scipy.sparse import csc_matrix

#from keras.utils import to_categorical
def oneHotify(matrix,index):
    array = matrix[:,index]
    dict_array = {}
    counter = 0
    for i in array:
        if i not in dict_array.keys():
            dict_array[i] = counter
            counter += 1
    
    for k in range(len(array)):
        array[k] = dict_array[array[k]]

    encoded = to_categorical(array) #encoded returns the OneHot matrix
    matrix = np.concatenate((matrix,encoded),axis=1) #append the OneHot matrix to the end
    matrix = np.delete(matrix,index,1) #delete the column of the index
    print(len(encoded[0]))
    return matrix


# In[ ]:


with open('claims_final.csv','r') as csvfile:
    wholefile = list(csv.reader(csvfile))


# In[ ]:


family_dict = {}
member_dict = {}
provider_dict = {}
type_dict = {}
state_dict = {}
procedure_dict = {}
f_counter = 0
s_counter = 0
m_counter = 0
p_counter = 0
t_counter = 0
pt_counter = 0
for i in range(len(wholefile)):
    for j in range(len(wholefile[i])):
        if (j != 4 and j != 7):
            wholefile[i][j] = int(wholefile[i][j])
        elif (j == 7):
            wholefile[i][j] = float(wholefile[i][j])
        if (j == 0):
            if (wholefile[i][j] in family_dict.keys()):
                wholefile[i][j] = family_dict[wholefile[i][j]]
            else:
                family_dict[wholefile[i][j]] = f_counter
                f_counter += 1
                wholefile[i][j] = family_dict[wholefile[i][j]]
        elif (j == 1):
            if (wholefile[i][j] in member_dict.keys()):
                wholefile[i][j] = member_dict[wholefile[i][j]]
            else:
                member_dict[wholefile[i][j]] = m_counter
                m_counter += 1
                wholefile[i][j] = member_dict[wholefile[i][j]]
        elif (j == 2):
            if (wholefile[i][j] in provider_dict.keys()):
                wholefile[i][j] = provider_dict[wholefile[i][j]]
            else:
                provider_dict[wholefile[i][j]] = p_counter
                p_counter += 1
                wholefile[i][j] = provider_dict[wholefile[i][j]]
        elif (j == 3):
            if (wholefile[i][j] in type_dict.keys()):
                wholefile[i][j] = type_dict[wholefile[i][j]]
            else:
                type_dict[wholefile[i][j]] = t_counter
                t_counter += 1
                wholefile[i][j] = type_dict[wholefile[i][j]]
        elif (j == 4):
            if (wholefile[i][j] in state_dict.keys()):
                wholefile[i][j] = state_dict[wholefile[i][j]]
            else:
                state_dict[wholefile[i][j]] = s_counter
                s_counter += 1
                wholefile[i][j] = state_dict[wholefile[i][j]]
        elif (j == 6):
            if (wholefile[i][j] in procedure_dict.keys()):
                wholefile[i][j] = procedure_dict[wholefile[i][j]]
            else:
                procedure_dict[wholefile[i][j]] = pt_counter
                pt_counter += 1
                wholefile[i][j] = procedure_dict[wholefile[i][j]]
            


# In[ ]:


truncated_columns = np.array(wholefile)


# In[ ]:


del wholefile


# In[ ]:


truncated_columns = truncated_columns[:, [1,2,3,4,6,7]]


# In[ ]:



def one_hot_encoding(a, num):
    temp = a[:, num]
    temp = set(list(temp))
    #print(temp)
    size = len(temp)
    modified = np.zeros((a.shape[0], a.shape[1]+size))
    print(modified.shape)
    modified[:, :-size] = a
    for i in range(a.shape[0]):
        modified[i, a.shape[1] + int(modified[i, num])] = 1
    #modified = np.delete(modified, num, 1)
    return modified


columns = [4,3,2,0,1]
for i in columns:
    #truncated_columns = oneHotify(truncated_columns, 1)
    truncated_columns = one_hot_encoding(truncated_columns, i)
    print('Done encoding column ' + str(i))

truncated_columns = truncated_columns[:,5:]
truncated_columns = csc_matrix(truncated_columns)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

X = truncated_columns[:, :-1]
y = truncated_columns[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
y_train = y_train.toarray()
y_test = y_test.toarray()
alphas = [1e-3,1e-2,1e-1,1,1e1,1e2]
errors = []
print('start training')
for alpha in alphas:
    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    errors.append(np.sum(np.abs(y_test-y_predict)))
    print(errors)
print(errors)
# In[ ]:



