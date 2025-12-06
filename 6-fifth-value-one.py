# 6.) Create a null vector of size 10 but the fifth value which is 1
import numpy as np
#meth 1:hard coded hhh
print(np.array([0,0,0,0,1,0,0,0,0,0]))
#meth 2:
r =np.zeros([10],dtype=int)
r[4] = 1
print(r)