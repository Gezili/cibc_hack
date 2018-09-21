import numpy as np
from keras.utils import to_categorical
def oneHotify(array):
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
	encoded = to_categorical(array)
	return encoded
	
if __name__ == '__main__':
	array = ['987425','2431534','100','100','2023']
	ans = oneHotify(array)
	print(array)
	print(ans)
	#output
# 	[0, 1, 2, 2, 3]
# 	[[1. 0. 0. 0.]
#  	 [0. 1. 0. 0.]
#    [0. 0. 1. 0.]
#    [0. 0. 1. 0.]
#    [0. 0. 0. 1.]]
