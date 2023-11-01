def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in xrange(2, n):
        if n % i == 0:
