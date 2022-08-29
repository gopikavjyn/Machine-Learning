print("20 Gopika Vijayan ")
n1=int(input("enter the no of rows of 1st matrix:"))
n2=int(input("enter the no of coloumns of 1st matrix:"))
print("Enter the elements")
matrix=[]
for i in range(0,n1):
    a=[]
    for j in range(0,n2):
        a.append(int(input()))
    matrix.append(a)
for i in range(0,n1):
    for j in range(0,n2):
        print(matrix[i][j], end = " ")
    print()
n1=int(input("Enter the number of rows for 2nd matix"))
n2=int(input("Enter the number of columns for 2nd matix"))
print("Enter the elements")
matrix2=[]

for i in range(0,n1):
    b=[]
    for j in range(0,n2):
        b.append(int(input()))
    matrix2.append(b)
for i in range(0,n1):
    for j in range(0,n2):
        print(matrix2[i][j], end = " ")
    print()
print("Matrix sum is:")
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, n1):
    for j in range(0, n2):
        result[i][j] = matrix[i][j] + matrix2[i][j]
for r in result:
    print(r)