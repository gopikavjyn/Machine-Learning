import numpy as np
ar=np.array([
    [0,0,0,0,1],
    [2,0,0,1,3],
    [4,0,2,0,0],
    [3,2,0,0,1]
])
print("\n",ar)
U,s,V=np.linalg.svd(ar,full_matrices=False)
print("singular value decomposition")
print("\nU=",U,"\n\ns=",s,"\n\nV=",V)