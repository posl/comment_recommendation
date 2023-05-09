def get_primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    #sieve of eratosthenes
    limit = n + 1
    not_prime = [False] * limit
    primes = []
    for i in range(2, limit):
        if not_prime[i]:
            continue
        for f in range(i * 2, limit, i):
            not_prime[f] = True
        primes.append(i)
    return primes
