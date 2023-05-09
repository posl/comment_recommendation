def solve(n, m, a):
    if m == 0:
        return 1
    a.sort()
    a = [0] + a + [n + 1]
    b = [a[i + 1] - a[i] - 1 for i in range(m + 1)]
    b = list(filter(lambda x: x > 0, b))
    k = min(b)
    return sum([b[i] // k for i in range(len(b))]) + len(b)
