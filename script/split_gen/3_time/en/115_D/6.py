def burger(n,x):
    if n==0:
        return 1
    elif n==1:
        return 0
    else:
        if x<=2**(n-1):
            return burger(n-1,x-1)
        elif x==2**(n-1)+1:
            return 2**(n-1)
        else:
            return 2**(n-1)+burger(n-1,x-2**(n-1)-1)
n,x=map(int,input().split())
print(burger(n,x))
