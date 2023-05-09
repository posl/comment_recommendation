def good(x, a, d, n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return min(good(x, a, d, n - 1) + 1, good(x, a, d, n // 2) + 2)
    else:
        return min(good(x, a, d, n - 1) + 1, good(x, a, d, (n + 1) // 2) + 2)
x, a, d, n = map(int, input().split())
print(good(x, a, d, n))
