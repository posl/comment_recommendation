def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return not any(n % i == 0 for i in range(3, int(n ** 0.5) + 1, 2))
