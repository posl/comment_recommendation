def get_input():
    N = int(input())
    x = []
    y = []
    p = []
    for i in range(N):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        p.append(c)
    return N, x, y, p
