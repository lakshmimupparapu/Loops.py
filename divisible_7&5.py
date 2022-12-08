# x=int(input("enter the number:"))
# y=int(input("enter the second number:"))
# while x<=y:
#     if x%7==0 and y%5==0:
#         print(x)
#     x+=1

# n=int(input("enter the number"))
# l=[]
# i=1
# while i<=n:
#     s=int(input("enter the number"))
#     l.append(s)
#     i=i+1
# i=0
# m1=0
# m2=0
# m3=0
# while i<len(l):
#     if l[i]>m1:
#         m1=l[i]
#     i=i+1
# j=0
# while j<len(l):
#     if l[j]>m2 and l[j]!=m1:
#         m2=l[j]
#     j=j+1
# k=0
# while k<len(l):
#     if l[k] >m3 and l[k]!=m1 and l[k]!=m2:
#         m3=l[k]
#     k=k+1

print(m1,m2,m3)
n=int(input())
s=[]
i=len(str(n))-1
for k in str(n):
    if k!=0:
        s.append(k+"0"*i)
    i=i-1
    x="+".join(s)
print(","+x+",")
