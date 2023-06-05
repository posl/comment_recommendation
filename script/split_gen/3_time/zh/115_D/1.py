def patty(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    mid = (1 << n + 2) - 3
    if x == mid + 2:
        return (1 << n + 1) - 1
    elif x > mid + 2:
        return (1 << n + 1) - 1 + patty(n - 1, x - mid - 2)
    else:
        return patty(n - 1, x - 1)
N, X = map(int, input().split())
print(patty(N, X))
