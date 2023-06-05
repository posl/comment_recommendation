def solve(n, k, x, a):
    sum = 0
    for i in range(n):
        sum += max(a[i] - x, 0)
    return sum
