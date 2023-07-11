def is_prime(n):
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
