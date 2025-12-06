#15.) Create a 2d array with 1 on the border and 0 inside
import numpy as np
r=np.array([1,2,3])
print(r)

rrr = np.r.shape(2)
print(rrr)
rr =np.pad(r,pad_wiidth=1,mode='constant',constant_values=0)
print(rr)