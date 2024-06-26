def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return pow(2, n-1, n) == 1
