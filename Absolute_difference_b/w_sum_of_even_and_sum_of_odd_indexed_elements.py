n=int(input())
so=0
se=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if i%2==1:
        so+=a[i]
    else:
        se+=a[i]
b=abs(so-se)
print(b)