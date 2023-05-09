def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    if n % 10 not in (0, 1, 4, 5, 6, 9):
        return False
    if n < 1024:
        return int(n ** 0.5) ** 2 == n
    r = int(n ** 0.5)
    return (r - 1) ** 2 < n <= r ** 2
