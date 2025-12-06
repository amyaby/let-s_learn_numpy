#4.) How to get the memory size of any array

import numpy as np
ar = np.array([1,2,3])
print(ar.size)#total number of elements 3
print(ar.nbytes)#`THE CORRECT ANSWER` :Total memory size (in bytes) 8*3=24
print(ar.itemsize)#size in bytes of each element 8
print(ar.shape)# dimenssions of the array 2d or 3d ..
print(ar.dtype)
# =>when we talk about the memory size of an array, we are referring to the total amount of memory it occupies in bytes.