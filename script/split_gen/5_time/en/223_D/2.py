def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.reverse()
    b.reverse()
    p = []
    for i in range(n):
        p.append(i+1)
    for i in range(m):
        if p.index(a[i]) > p.index(b[i]):
            p[p.index(a[i])], p[p.index(b[i])] = p[p.index(b[i])], p[p.index(a[i])]
    print(*p)
