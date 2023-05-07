def prime_factorize(n):
    """Return a list of the prime factorization of a positive integer."""
    if n < 2:
        return []
    factorization = []
    while n % 2 == 0:
        factorization.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            factorization.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        factorization.append(n)
    return factorization
