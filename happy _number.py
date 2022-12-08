n=int(input("enter the number:"))
temp=n
# sum=0
while temp>=10:
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+(digit**2)
        temp=temp//10
    temp=sum
if sum==1:
    print("happy number")
else:
    print("unhappy number")