def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
