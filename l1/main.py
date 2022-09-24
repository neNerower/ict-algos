from timeit import timeit
import numpy as np

from transpont import transpont
from multiply import mult
from rank import get_matrix_rank


a = np.arange(15).reshape(5,3)
b = np.arange(12).reshape(3,4)

print("Matrix a:")
print(a)
print("\n\nMatrix b:")
print(b)

# Numpy way
print("\n\nTransposed matrix a:")
print(a.transpose())

print("\n\nMultiply matrix a with b:")
print(np.dot(a,b))

print("\n\nRank of matrix a:")
print(np.linalg.matrix_rank(a))


### Time it
# My way
setup = '''
from inverse import inverse
import numpy as np
m = [
    [ 2,  5,  7],
    [ 6,  3,  4],
    [ 5, -2, -3]
]
'''
me = timeit('inverse(m)', setup, number=1000)

# Numpy way
npy = timeit('np.linalg.inv(m)', setup, number=1000)

print(f"\n\nMy way: {me} seconds")
print(f"\n\nNumpy way: {npy} seconds")