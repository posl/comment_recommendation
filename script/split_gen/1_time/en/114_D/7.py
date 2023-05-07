def prime_factorization(n):
    if n == 1:
        return {}
    prime_factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            if i in prime_factors:
                prime_factors[i] += 1
            else:
                prime_factors[i] = 1
        i += 1
    if n > 1:
        prime_factors[n] = 1
    return prime_factors
