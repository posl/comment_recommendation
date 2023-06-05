def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i = i+2
    return True
