n=int(input())
s=n%10
n=n//10
l=n%10
n=n//10
if s%2==0 and l%2==0 and n%2==0:
    print('Even')
elif s%2!=0 and l%2!=0 and n%2!=0:
    print('Odd')
else:
    print('Mixed')
    