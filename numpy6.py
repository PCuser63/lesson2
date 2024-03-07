import numpy as np
def nonzero(A):
    x = np.nonzero(A)
    return x

A = np.zeros((100,100))
A[56,70] = 1
print(nonzero(A))
