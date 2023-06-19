def prime_factorization(n):
    prime_factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n /= i
        i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors
