def solve(n, a):
    x = [0] * n
    for i in range(n):
        x[i] = a[i] - sum(x) * 2
    return x
