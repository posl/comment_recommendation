def f(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+2*f(n-1,(1+2**(n+1))-x):
        return f(n-1,x-1)
    else:
        return 2**n+f(n-1,(1+2**(n+1))-x-1)
n,x=map(int,input().split())
print(f(n,x))
