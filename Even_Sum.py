n=int(input())
so=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]%2==0:
        so+=a[i]
print(so)