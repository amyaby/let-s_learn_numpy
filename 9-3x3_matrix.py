#9.) Create a 3x3 Matrix with values ranging from 0 to 8
import numpy as np
r = np.arange(0,9)
print(r.reshape(3,3))
#reshape(row,column) chnages the array's shape to a matrix 