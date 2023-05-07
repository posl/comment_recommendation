def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N):
        b[i] = a[i]
    b.sort()
    c = [0] * N
    for i in range(N):
        c[i] = b[i]
    for i in range(N):
        c[i] = c[i] + c[i - 1]
    d = [0] * N
    for i in range(N):
        d[i] = c[i]
    for i in range(N):
        d[i] = d[i] - c[i - 1]
    e = [0] * N
    for i in range(N):
        e[i] = d[i]
    for i in range(N):
        e[i] = e[i] + e[i - 1]
    f = [0] * N
    for i in range(N):
        f[i] = e[i]
    for i in range(N):
        f[i] = f[i] - e[i - 1]
    g = [0] * N
    for i in range(N):
        g[i] = f[i]
    for i in range(N):
        g[i] = g[i] + g[i - 1]
    h = [0] * N
    for i in range(N):
        h[i] = g[i]
    for i in range(N):
        h[i] = h[i] - g[i - 1]
    i = [0] * N
    for i in range(N):
        i[i] = h[i]
    for i in range(N):
        i[i] = i[i] + i[i - 1]
    j = [0] * N
    for i in range(N):
        j[i] = i[i]
    for i in range(N):
        j[i] = j[i] - i[i - 1]
    k = [0] * N
    for i in range(N):
        k[i] = j[i]
    for i in range(N):
        k[i] = k[i] + k[i - 1]
    l = [0] * N
    for i in range(N):
        l[i] = k[i]
    for i in range(N):
        l[i] = l[i]

if __name__ == '__main__':
    main()