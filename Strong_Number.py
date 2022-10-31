a=int(input())
b=a
s=0
while a!=0:
    r=a%10
    d=1
    for i in range(1,r+1):
        d*=i
    s+=d
    a=a//10
if s==b:
    print("The number",b, "is a strong number")

else:
    print('The number',b,'is not a strong number')