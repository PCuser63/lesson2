import numpy as np

def closest(vecs,v,r):
    position = vecs[v]
    distances = np.linalg.norm(vecs - position,axis = 1)
    count = np.sum(distances<r)
    return count

vecs = np.array([[0.71, 0.7, 0.22, 0.98, 0.01]])

r = 0.1
v = 0
result = closest(vecs, v, r)
print(result)
