def calc(n, p, q):
    p = [i-1 for i in p]
    q = [i-1 for i in q]
    p = [p.index(i) for i in range(n)]
    q = [q.index(i) for i in range(n)]
    return abs(p.index(0) - q.index(0))
