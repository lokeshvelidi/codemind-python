x,y=map(int,input().split())
m=0
for i in range(1,max(x,y)):
    if x%i==0 and y%i==0:
        if m<i:
            m=i
print(m)