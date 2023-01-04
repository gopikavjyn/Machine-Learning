import numpy as np
m1=np.array([
    [1,2,3],
    [6,7,8],
    [1,4,5]
])
m2=np.array([
    [9,7,6],
    [3,4,5],
    [4,5,6]
])
print("Matrix 1:\n",m1)
print("Matrix 2:\n",m2)
a1=np.add(m1,m2)
print("after add",a1)
a2=np.subtract(m1,m2)
print("after sub ",a2)
a3=np.multiply(m1,m2)
print("after mul",a3)
a4=np.divide(m1,m2)
print("after div",a4)
a5=np.matmul(m1,m2)
print("matrix mul",a5)
print("transpose of 1st matrix:",np.transpose(m1))
print("transpose of 2nd matrix:",np.transpose(m2))
print("sum of diag elem of mat 1:",np.trace(m1))
print("sum of diag elem of mat 1:",np.trace(m2))