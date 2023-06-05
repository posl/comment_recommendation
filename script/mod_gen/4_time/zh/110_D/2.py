def prime_factorization(n):
    prime_factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 1:
        prime_factors.append(n)
    return prime_factors

if __name__ == '__main__':
    prime_factorization()