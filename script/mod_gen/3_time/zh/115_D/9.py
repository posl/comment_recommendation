def burger(n,x):
    if x==1 and n==1:
        return 0
    elif x==1 and n!=1:
        return 0
    elif x==2**(n+1)-1:
        return 2**n
    elif x==2**(n+1)-2:
        return 2**n-1
    elif x>2**(n+1)-2:
        return 2**n-1+burger(n-1,x-(2**(n+1)-2))
    elif x<2**(n+1)-2:
        return burger(n-1,x-1)
n,x=map(int,input().split())
print(burger(n,x))
