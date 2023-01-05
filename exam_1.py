print("20 Gopika Vijayan")
import numpy as np
x = np.array([
    [3, 4, 5],
    [2, 8, 5],
    [5, 6, 3]
])
print("First Matrix is:", x)
y = np.array([
    [2, 5, 6],
    [4, 7, 8],
    [6, 7, 3]
])
print("Second Matrix is:", y)
a = (7*x)+(y**3)
print("Operation 7x+y:", a)
b=np.matmul(x, y)
print("Matrix multiplication:", b)
c = np.diag(x)
print("diagonal elements of 1st matrix:", c)
d = np.diag(y)
print("diagonal elements of 2nd matrix:", d)
e = np.linalg.matrix_rank(x)
print("Rank of 1st matrix is:", e)
f=np.linalg.matrix_rank(y)
print("Rank of 2nd matrix is:", f)
