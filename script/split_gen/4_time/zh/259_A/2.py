def solve(n, m, x, t, d):
    h = t
    for i in range(x, m):
        h += d
    for i in range(m, n):
        h += d
    return h
