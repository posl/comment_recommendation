def solve(n, m, a):
    if m == 0:
        return 1
    a.sort()
    b = [a[0] - 1]
    for i in range(1, m):
        b.append(a[i] - a[i - 1] - 1)
    b.append(n - a[m - 1])
    d = max(b)
    return (d + 1) // 2 + 1
