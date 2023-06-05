def get_prime_factors(n):
    prime_factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            prime_factors.append(i)
            n = n // i
    return prime_factors

if __name__ == '__main__':
    get_prime_factors()