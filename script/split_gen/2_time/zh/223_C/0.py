def solve(n, a, b):
    total = 0
    for i in range(n):
        total += a[i] / b[i]
    half = total / 2
    sum = 0
    for i in range(n):
        sum += a[i] / b[i]
        if sum > half:
            return sum * b[i] - (sum - half) * b[i]
    return 0
