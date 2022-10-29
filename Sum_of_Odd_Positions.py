n=int(input())
so=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if i%2==1:
        so+=a[i]
print(so)