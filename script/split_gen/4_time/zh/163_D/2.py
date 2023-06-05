def f(n, k):
    if n < k:
        return 0
    elif n == k:
        return 1
    else:
        return f(n - 1, k) + f(n - 1, k - 1)
n, k = map(int, input().split())
print(f(n, k) % 1000000007)
