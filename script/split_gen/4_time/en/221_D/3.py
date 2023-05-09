def solve(n, ab):
    d = {}
    for a, b in ab:
        d[a] = d.get(a, 0) + 1
        d[a + b] = d.get(a + b, 0) - 1
    result = [0] * n
    c = 0
    for i in range(1, 10**9 + 1):
        c += d.get(i, 0)
        result[c - 1] += 1
    return result
