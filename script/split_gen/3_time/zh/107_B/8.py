def solve():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = []
    for i in range(H):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for j in range(W):
        if '#' in [b[i][j] for i in range(len(b))]:
            c.append([b[i][j] for i in range(len(b))])
    for i in range(len(c)):
        print(''.join(c[i]))
