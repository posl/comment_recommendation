def get_prime_factorization(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime_factors.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_factors.append(n)
    return prime_factors

if __name__ == '__main__':
    get_prime_factorization()