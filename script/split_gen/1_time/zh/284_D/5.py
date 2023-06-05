def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n ** 0.5) + 1
    for i in range(3, sqr, 2):
        if n % i == 0:
            return False
    return True
