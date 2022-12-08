user=int(input("enter the prime number:"))
i=1
c=0
while i<=user:
    if user%i==0:
        c=c+1
    i+=1
if c==2:
    print(user,"is prime number")
else:
    print(user," is not prime number")