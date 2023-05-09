def solve(n, m, a, c):
    b = [0 for _ in range(m + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            b[j] += a[i] * c[i + j]
    return b
