n=int(input())
s=1
a=0
for i in str(n):
    s*=int(i)
    a+=int(i)
if s==a:
    print("Spy Number")
else:
    print('Not Spy Number')