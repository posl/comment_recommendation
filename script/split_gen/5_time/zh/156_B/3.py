def get_digit(n, k):
    if n == 0:
        return 0
    return get_digit(n//k, k) + 1
