laxmi=int(input("enter the number:"))
sum=0
temp=laxmi
while temp>0:
    digit=temp%10
    sum=sum*10+digit
    temp=temp//10
if sum==laxmi:
    print(laxmi,"is polindrome number")
else:
    print(laxmi,"is not polindrome number")
