def isPrime(n):
    if n <= 1:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 6 != 1 and n % 6 != 5:
        return 0
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return 0
        i += 6
    return 1
