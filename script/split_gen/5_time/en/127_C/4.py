def solve():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    print(max(0, min(r) - max(l) + 1))
