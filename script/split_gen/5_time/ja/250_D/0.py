def primeFactorization(n):
    if n == 1:
        return []
    factor = []
    i = 2
    while i*i <= n:
        while n%i == 0:
            n //= i
            factor.append(i)
        i += 1
    if n > 1:
        factor.append(n)
    return factor
