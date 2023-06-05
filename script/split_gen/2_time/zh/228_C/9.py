def f(n,x,l):
    d = {}
    for i in range(n):
        d[i+1] = 0
    d[x] = 1
    for i in range(n):
        if d[l[i]] == 1:
            d[i+1] = 1
    return sum(d.values())
