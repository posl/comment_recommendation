def get_prime_factors(n):
    pf = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            pf.append(i)
            n = n // i
    if n > 1:
        pf.append(n)
    return pf
