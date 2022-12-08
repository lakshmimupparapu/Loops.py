n=int(input("enter the number:"))
i=1
a=1
while i<=n:
    j=1
    while j<=i:
        print(a,end=" ")
        j=j+1
    a=a+2
    i=i+1
    print()