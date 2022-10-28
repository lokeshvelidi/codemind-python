n=int(input())
for i in range(n):
    a=int(input())
    b=(a)**(0.5)
    if a%b==0:
        print('True')
    else:
        print('False')