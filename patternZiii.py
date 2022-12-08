n=int(input("enter the number :"))
i=5
while i>=1:
    k=1
    while k<=n-i:
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    i=i-1
    print()