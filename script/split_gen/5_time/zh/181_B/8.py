def solve(n, a, b):
    total = 0
    for i in range(n):
        total += (b[i] - a[i] + 1) * (a[i] + b[i]) // 2
    return total
