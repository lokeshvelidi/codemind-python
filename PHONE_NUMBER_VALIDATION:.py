n=input()
lst=list(n)
if len(lst)==10:
    if lst[0]!=0:
        print('Valid')
else:
    print('Invalid')