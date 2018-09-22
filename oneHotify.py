import numpy as np
from keras.utils import to_categorical
def oneHotify(matrix,index):
    array = matrix[:,index]
    dict_array = {}
    counter = 0
    for i in array:
        if i not in dict_array.values():
            dict_array[counter] = i
            counter += 1
        else:
            continue
    for key, value in dict_array.items():
        for i in range(len(array)):
            if value == array[i]:
                array[i] = key
    encoded = to_categorical(array) #encoded returns the OneHot matrix
    matrix = np.concatenate((matrix,encoded),axis=1) #append the OneHot matrix to the end
    matrix = np.delete(matrix,index,1) #delete the column of the index
    print(len(encoded[0]))
    return matrix

if __name__ == '__main__':
    matrix = np.array([[987425,2431534,100,100,2023],
                       [234534,2332141,100,200,2023],
                       [234534,2332141,150,200,2023]])
    index = 2
    ans = oneHotify(matrix,index)
    # print(matrix)
    print(ans)
    #output (if input strings)
# [['987425' '2431534' '100' '2023' '1.0' '0.0']
#  ['234534' '2332141' '200' '2023' '1.0' '0.0']
#  ['234534' '2332141' '200' '2023' '0.0' '1.0']]
