import numpy as np
ar=np.array([
    [1,2,3,4],
    [4,6,7,3],
    [8,9,0,1],
    [5,6,3,2]
])
print("matrix\n",ar)
a1=ar[1:4]
print("\n",a1)
a2=ar[:,0:3]
print("\n",a2)
print("elem of mid",ar[1:3,0:2])
a3=ar[:,1:3]
print("\n",a3)
print("\n",ar[0,1:3])
