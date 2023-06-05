def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    x = 3
    while x * x <= n:
        if n % x == 0:
            return False
        x += 2
    return True
