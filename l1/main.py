from transpont import transpont
from multiply import mult
from rank import get_matrix_rank

import numpy as np


a = np.arange(15).reshape(5,3)
b = np.arange(12).reshape(3,4)

print("Matrix a:")
print(a)
print("\n\nMatrix b:")
print(b)

print("\n\nTransposed matrix a:")
print(a.transpose())


print("\n\nMultiply matrix a with b:")
print(np.dot(a,b))

print("\n\nRank of matrix a:")
print(np.linalg.matrix_rank(a))

