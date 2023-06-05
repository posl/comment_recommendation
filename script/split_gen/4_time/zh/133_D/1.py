def solve(n, a):
    b = [0] * n
    for i in range(n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    b[0] //= 2
    for i in range(1, n):
        b[i] = a[i-1] - b[i-1]
    for i in range(n):
        b[i] *= 2
    return b
