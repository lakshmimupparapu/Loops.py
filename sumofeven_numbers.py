# a=int(input("enter the number:"))
# b=int(input("enter the second number:"))
# sum=0
# while a<=b:
#     if a%2==0:
#         sum=sum+a
#     a+=1
#     print(sum)


numbers=[50,40,23,70,560,12,5,10,7]
i=0
b=0
while i<len(numbers):
    if numbers[i]>b:
        b=numbers[i]
    i=i+1
print(b)