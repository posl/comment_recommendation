def f(n):
    if n==1:
        return True
    if n%2==0:
        return f(n/2)
    if n%2==1:
        return f(n-1)
