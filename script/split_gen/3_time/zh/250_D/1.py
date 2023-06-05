def isPrime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for p in range(3, int(n**0.5)+1, 2):
        if n % p == 0: return False
    return True
