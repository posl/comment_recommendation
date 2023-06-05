def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + a[i]
    c = [0] * (n + 1)
    for i in range(1, n + 1):
        c[i] = max(c[i - 1], b[i])
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        d[i] = max(d[i - 1], c[i] + b[i])
    e = [0] * (n + 1)
    for i in range(1, n + 1):
        e[i] = max(e[i - 1], d[i] + b[i])
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        f[i] = max(f[i - 1], e[i] + b[i])
    g = [0] * (n + 1)
    for i in range(1, n + 1):
        g[i] = max(g[i - 1], f[i] + b[i])
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = max(h[i - 1], g[i] + b[i])
    i = [0] * (n + 1)
    for i in range(1, n + 1):
        i[i] = max(i[i - 1], h[i] + b[i])
    j = [0] * (n + 1)
    for i in range(1, n + 1):
        j[i] = max(j[i - 1], i[i] + b[i])
    k = [0] * (n + 1)
    for i in range(1, n + 1):
        k[i] = max(k[i - 1], j[i] + b[i])
    l = [0] * (n + 1)
    for i in range(1, n +

if __name__ == '__main__':
    main()