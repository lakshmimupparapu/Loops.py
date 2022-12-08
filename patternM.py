n=int(input("enter the number:"))
i=1
sum=1
while i<=n:
    j=1
    while j<=i:
        print(sum,end=" ")
        sum=sum+1
        j=j+1
    i=i+2
    print()