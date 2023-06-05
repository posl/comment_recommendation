def get_primes(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
