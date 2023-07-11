def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n == 1:
        return False
    else:
