def get_prime_factors(n):
    factors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

if __name__ == '__main__':
    get_prime_factors()