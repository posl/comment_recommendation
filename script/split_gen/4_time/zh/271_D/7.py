def f(n,s,a):
    if n==0: return s==0
    if f(n-1,s-a[n-1]): return True
    if f(n-1,s): return True
    return False
