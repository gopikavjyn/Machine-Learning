print("20 Gopika Vijayan ")
n1=int(input("enter lower limit:"))
n2=int(input("enter upper limit:"))
for i in range(n1 , n2):
   for j in range(2 , i):
      if(i % j) == 0:
       print(i)
       break

