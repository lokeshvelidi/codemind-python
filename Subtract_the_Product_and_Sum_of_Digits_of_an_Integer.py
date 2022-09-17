n=int(input())
s=1
a=0
for i in str(n):
    s*=int(i)
    a+=int(i)
print(s-a)
    