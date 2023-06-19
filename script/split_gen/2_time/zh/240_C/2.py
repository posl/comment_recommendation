def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    d = [0] * (x + 1)
    d[0] = 1
    for i in range(n):
        for j in range(a[i], x + 1):
            if d[j - a[i]]:
                d[j] = 1
        for j in range(b[i], x + 1):
            if d[j - b[i]]:
                d[j] = 1
    if d[x]:
        print('Yes')
    else:
        print('No')
