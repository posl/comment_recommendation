def solve(n, m, a):
    if m == 0:
        return 1
    a.sort()
    a.append(n + 1)
    k = 1
    b = []
    for i in range(m):
        if a[i + 1] - a[i] - 1 > 0:
            b.append(a[i + 1] - a[i] - 1)
    return (max(b) + k - 1) // k
