def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True
