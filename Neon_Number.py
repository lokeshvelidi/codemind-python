n=int(input())
a=n*n
s=0
while a>0:
    b=a%10
    s=s+b
    a=a//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")