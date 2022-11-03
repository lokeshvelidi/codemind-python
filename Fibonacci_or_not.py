n=int(input())
c=0
a=1
b=1
while n>c:
    c=a+b
    b=a
    a=c
if n==c:
    print("True")
else:
    print('False')