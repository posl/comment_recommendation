def min_value(n, k):
    if n == 0:
        return 0
    return min(n % k, k - n % k)
