def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        else:
            i += 2
    return True
