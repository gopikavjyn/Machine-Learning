print("20 Gopika Vijayan ")
n1=int(input("enter the list 1 size:"))
list1=[]
print("enter the values of list 1:")
for i in range(0,n1):
   x=int(input())
   list1.append(x)
n2=int(input("enter the list 2 size:"))
list2=[]
print("enter the values of list 2")
for i in range(0,n2):
   y=int(input())
   list2.append(y)
print(list1)
print(list2)
list3=[]
if n1==n2:
   for i in range(0,n1):
       element=list1[i]+list2[i]
       list3.append(element)
   print(list3)
else:
   print("No of elements are not equal")
