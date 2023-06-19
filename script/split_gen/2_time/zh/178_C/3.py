def get_combinations_count(n, r):
    if n < r:
        return 0
    if r == 0:
        return 1
    return get_combinations_count(n - 1, r - 1) * n // r
