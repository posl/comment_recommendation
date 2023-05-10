def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*n
    for i in range(n):
        b[i] = a[i]%m
    b.sort()
    c = [0]*n
    for i in range(n):
        c[i] = b[i] + m
    d = [0]*n
    for i in range(n):
        d[i] = c[i] - b[i]
    e = [0]*n
    for i in range(n):
        e[i] = d[i] - m
    f = [0]*n
    for i in range(n):
        f[i] = e[i] - b[i]
    g = [0]*n
    for i in range(n):
        g[i] = f[i] - m
    h = [0]*n
    for i in range(n):
        h[i] = g[i] - b[i]
    i = 0
    while i < n:
        if h[i] < 0:
            h[i] = 0
        i += 1
    j = 0
    while j < n:
        if h[j] < 0:
            h[j] = 0
        j += 1
    k = 0
    while k < n:
        if h[k] < 0:
            h[k] = 0
        k += 1
    l = 0
    while l < n:
        if h[l] < 0:
            h[l] = 0
        l += 1
    m = 0
    while m < n:
        if h[m] < 0:
            h[m] = 0
        m += 1
    n = 0
    while n < n:
        if h[n] < 0:
            h[n] = 0
        n += 1
    o = 0
    while o < n:
        if h[o] < 0:
            h[o] = 0
        o += 1
    p = 0
    while p < n:
        if h[p] < 0:
            h[p] = 0
        p += 1
    q = 0
