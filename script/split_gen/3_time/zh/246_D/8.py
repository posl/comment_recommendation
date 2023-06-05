def f(N):
    if N==0:
        return 0
    l = 0
    r = 10**18
    while r-l>1:
        m = (l+r)//2
        if m**3+m**2*m+m*m**2+m**3<N:
            l = m
        else:
            r = m
    return r
N = int(input())
print(f(N))
