def solve(a, c):
    n = len(a) - 1
    m = len(c) - 1
    b = [0] * (m + 1)
    for j in range(m, n, -1):
        b[j - n] = c[j] // a[n]
        for i in range(n + 1):
            c[i + j - n] -= b[j - n] * a[i]
    return b
