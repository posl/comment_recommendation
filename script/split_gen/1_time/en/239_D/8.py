def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i <= n**0.5:
        if n % i == 0: return False
        i += 2
    return True
