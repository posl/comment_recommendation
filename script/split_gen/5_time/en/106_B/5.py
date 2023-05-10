def prime_factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n = n // f
        else:
            f += 2
    if n != 1:
        factors.append(n)
    return factors
