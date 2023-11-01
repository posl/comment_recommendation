def primeSieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
