#8.) Reverse a vector (first number becomes last)
#meth 1 : not recommended
import numpy as np
r = [1,2,3,4,5,6]
length = len(r)
for l in range(length//2) :
    x =r[l]
    r[l]=r[length-l-1] #     r[l], r[length - l - 1] = r[length - l - 1], r[l]
    r[length-l-1] = x 
print(r)
#meth 2 : slicing (recommended)
r = [1,2,3,4,5,6]
print(r[::-1])# does not modify the original list (creates a copy)
#[::-1] creates a new reversed copy of the list.
#-1: means the last element
#reverse() modifies the original list and returns None.
#Breaking Down [::-1]

#First :: Omit the start index, so it defaults to the beginning of the sequence.
#Second :: Omit the stop index, so it defaults to the end of the sequence.
#-1: The step is -1, which means:

#Traverse the sequence backwards (from the end to the start).
#Essentially, it reverses the sequence.


