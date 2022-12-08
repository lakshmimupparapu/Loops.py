user=int(input("enter the number"))
a=len(str(user))
sum=0
temp=user
while temp>0:
    digit=temp%10
    sum=sum+digit**a
    temp=temp//10
if user==sum:
    print(user,"is armstrong number")
else:
    print(user,"is not armstrong number")