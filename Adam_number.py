n=int(input())
s=0
a=str(n*n)
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
d=s*s
if a[::-1]==str(d):
    print('True')
else:
    print('False')
