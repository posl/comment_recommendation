def height(n,m,x,t,d):
    if n == m:
        return t
    else:
        for i in range(m,n):
            t += d
            if i == x:
                d = 0
        return t
