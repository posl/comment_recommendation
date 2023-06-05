def f(n,p):
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    return q
