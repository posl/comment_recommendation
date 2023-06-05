def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * n
    for i in range(n):
        b[i] = a[i] % m
    b.sort()
    c = [0] * n
    for i in range(n):
        c[i] = (b[i] + 1) % m
    c.sort()
    d = [0] * n
    for i in range(n):
        d[i] = (c[i] + 1) % m
    d.sort()
    e = [0] * n
    for i in range(n):
        e[i] = (d[i] + 1) % m
    e.sort()
    f = [0] * n
    for i in range(n):
        f[i] = (e[i] + 1) % m
    f.sort()
    g = [0] * n
    for i in range(n):
        g[i] = (f[i] + 1) % m
    g.sort()
    h = [0] * n
    for i in range(n):
        h[i] = (g[i] + 1) % m
    h.sort()
    i = [0] * n
    for i in range(n):
        i[i] = (h[i] + 1) % m
    i.sort()
    j = [0] * n
    for i in range(n):
        j[i] = (i[i] + 1) % m
    j.sort()
    k = [0] * n
    for i in range(n):
        k[i] = (j[i] + 1) % m
    k.sort()
    l = [0] * n
    for i in range(n):
        l[i] = (k[i] + 1) % m
    l.sort()
    m = [0] * n
    for i in range(n):
        m[i] = (l[i] + 1) % m
    m.sort()
    n = [0] * n
    for i in range(n):
        n[i] = (m[i] + 1) % m
    n.sort()
    o = [0] * n

if __name__ == '__main__':
    main()