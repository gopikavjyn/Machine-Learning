import numpy as np
array=np.random.randint(10,size=(3,3))
print("matrix is",array)
a1=np.linalg.inv(array)
print("inverse",a1)
a2=np.linalg.det(array)
print("determinant",a2)
a3=np.linalg.matrix_rank(array)
print("rank",a3)
r=array.flatten();
print("1d array",r)
u,v=np.linalg.eig(array)
print("eigon value",u)
print("eigon vector",v)