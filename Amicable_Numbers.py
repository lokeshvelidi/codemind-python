a=int(input())
b=int(input())
s=d=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range(1,b):
    if b%j==0:
        d+=j
if s==b and d==a:
    print('Amicable')
else:
    print('Not Amicable')
        