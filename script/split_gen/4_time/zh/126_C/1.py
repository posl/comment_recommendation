def solve(n,k):
    p = 0
    for i in range(1,n+1):
        t = 0
        while i < k:
            i *= 2
            t += 1
        p += (1/n)*(1/2)**t
    return p
