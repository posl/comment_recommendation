def is_prime(n):
    if n == 1:
        return False
    else:
        for k in range(2,n):
            if n % k == 0:
                return False
        return True
