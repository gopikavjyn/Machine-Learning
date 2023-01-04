import numpy as np
x=np.array([
    [2,3],
    [3,4],

])
print("matr\n",x)
a1=np.multiply(x,np.multiply(x,x))
print("cube-muliply fn\n",a1)
a2=np.power(x,3)
print("using power fn\n",a2)
a3=x**3
print("using **\n",a3)
a4=x*x*x
print("using *\n",a4)
a5=np.identity(2,dtype=int)
print("identity matr\n",a5)
a6=np.power(x,[[1,2],[3,4]])
print("powr",a6)
y=np.array([
    [3,7],
    [8,9]
])
a7=(x**2)+(2*y)
print("x2+2y operation:\n",a7)