n=int(input())
for i in range(n):
    b=int(input())
    a=b
    while True:
        pr=True
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                pr=False
                break
        if pr == True:
            break
        else:
            a+=1
            
            
    c=b
    while True:
        pr=True
        for i in range(2,int(c**0.5)+1):
            if c%i==0:
                pr=False
                break
        if pr == True:
            break
        else:
            c-=1
    d=b-c
    e=a-b
    if e>=d:
        print(c)
    else:
        print(a)