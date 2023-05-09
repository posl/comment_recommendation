def get_factors(n):
    factors = {}
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors[i] = 0
            while n % i == 0:
                n //= i
                factors[i] += 1
    if n > 1:
        factors[n] = 1
    return factors
