num=int(input("enter the perfect number:"))
sum=0
i=1
while num>i:
    if num%i==0:
        sum=sum+i
    i+=1
if sum==num:
    print(num,"is perfect number")
else:
    print(num,"is not perfect number")


