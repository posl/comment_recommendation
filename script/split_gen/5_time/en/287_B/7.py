def problem():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    print(len(set(s) & set(t)))
problem()
