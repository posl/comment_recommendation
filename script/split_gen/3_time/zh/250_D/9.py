def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n == 1:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True
