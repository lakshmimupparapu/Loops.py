user=int(input("enter the number:"))
temp=user
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit
    temp=temp//10
if user%sum==0:
    print(user,"is harshad number")
else:
    print(user,"is not harshad number")


