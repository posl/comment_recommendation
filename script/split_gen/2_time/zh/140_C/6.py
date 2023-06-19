def solve(n, b):
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n-1):
        a[i] = max(b[i-1], b[i])
    a[n-1] = b[n-2]
    return sum(a)
