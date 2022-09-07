a=int(input())
c= 0
for i in range(a):
    for j in range(a):
        if (i**2)+(j**2)==a:
            c+=1
if c==0:
    print("False")
else:
    print("True")