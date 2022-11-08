n=int(input())
for j in range(n):
    a=int(input())
    s=1
    for i in range(1,a+1):
        s*=i
    print(s)