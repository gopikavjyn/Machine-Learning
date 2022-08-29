print("20 Gopika Vijayan ")
num=int(input("enter number:"))

def digitsum(num):
    sum=0
    while num>0:
        rem=num%10;
        sum=sum+rem;
        num=num//10
    return sum
while(num>0):
    sum=digitsum(num)
    print("{} - {} = {}".format(num,sum,num-sum))
    num=num-sum