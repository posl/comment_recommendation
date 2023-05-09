def get_primes(n):
    # Sieve of Eratosthenes
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]
