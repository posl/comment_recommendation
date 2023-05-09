def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
