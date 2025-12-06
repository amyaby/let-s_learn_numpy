#10.) Find indices of non-zero elements from array
import numpy as np 
#MY answer 1: only native python lists :(
"""
r=[1,2,0,0,4,0]
for i,v in enumerate(r):#enumerate count indexes
    if v != 0:
        print(i)
    else:
        pass"""
arr = np.array([1,2,0,0,4,0])
#answer 2: using where
#result = np.where(arr!=0)
# answer 3: using nonzero  
result = np.nonzero(arr) 
print(result) 
"""Both np.nonzero() and np.where() return a tuple of arrays because they are designed to work with multi-dimensional arrays."""
# enumerate start counting indexes from the first one which is 0
# however u can chnage the default index to any number u want so instead od starting the array with 0 u start with 5,6,7...
#example : enumerate(r,start=3)