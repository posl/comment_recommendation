def f(n, k):
    if n < k:
        return 0
    if n == k:
        return 1
    return f(n-1, k) + f(n-1, k-1)
