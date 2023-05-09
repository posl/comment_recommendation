def primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    if n % 2 == 0:
        n += 1
    primes = [2, 3]
    for i in range(5, n, 2):
        for p in primes:
            if i % p == 0:
                break
            if p * p > i:
                primes.append(i)
                break
    return primes
