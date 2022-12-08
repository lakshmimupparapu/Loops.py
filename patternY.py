# n=int(input("enter the number:"))
i=1
while i<=7:
    print(" "*(7-i),end=" ")
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i+2
    print()
