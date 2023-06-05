def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True
