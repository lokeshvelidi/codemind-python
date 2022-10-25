n=int(input())
for i in range(1,n):
    a=(i*(i+1))
    if a==n:
         print('YES')
         break
if a!=n:
    print('NO')