


import numpy as np
import copy
import csv


from keras.utils import to_categorical
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
provider_dict = {}
type_dict = {}
state_dict = {}
procedure_dict = {}
f_counter = 0
s_counter = 0
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


columns = [4,3,2,1,0]
for i in range(1):
    truncated_columns = oneHotify(truncated_columns, 1)
    #truncated_columns = one_hot_encoding(truncated_columns, i)
    print('Done encoding column ' + str(i))


def one_hot_encoding(a, num):
    temp = a[:, num]
    temp = set(list(temp))
    size = len(temp)
    modified = np.zeros((a.shape[0], a.shape[1]+size))
    print(modified.shape)
    modified[:, :-size] = a
    for i in range(a.shape[0]):
        if (i%1000 == 0):
            print(i)
        modified[i, a.shape[1] + int(modified[i, num])] = 1
    #modified = np.delete(modified, num, 1)
    return modified


# In[ ]:


def one_hot_encoding(a, nums):
    temp = a[:, num]
    temp = set(list(temp))
    size = len(temp)
    modified = np.zeros((a.shape[0], a.shape[1]+size))
    print(modified.shape)
    modified[:, :-size] = a
    for i in range(a.shape[0]):
        if (i%1000 == 0):
            print(i)
        modified[i, a.shape[1] + int(modified[i, num])] = 1
    #modified = np.delete(modified, num, 1)
    return modified

