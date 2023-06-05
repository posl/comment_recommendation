def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif not n & 1:
        return False
    i = 3
    while i * i <= n:
        if not n % i:
            return False
        i += 2
    return True
