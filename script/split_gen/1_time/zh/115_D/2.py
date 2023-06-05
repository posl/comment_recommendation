def f(n,x):
    if n==0:
        return 0 if x<=0 else 1
    elif x<=1+2*f(n-1,2**(n-1)-1):
        return f(n-1,x-1)
    else:
        return 1+2*f(n-1,2**(n-1)-1)+f(n-1,x-2-2*f(n-1,2**(n-1)-1))
