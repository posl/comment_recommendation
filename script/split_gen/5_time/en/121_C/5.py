def get_input():
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    return n, m, a, b
