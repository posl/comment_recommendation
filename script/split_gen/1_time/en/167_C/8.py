def read_data():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(0)
        a.append([])
        c[i], *a[i] = map(int, input().split())
    return n, m, x, c, a
