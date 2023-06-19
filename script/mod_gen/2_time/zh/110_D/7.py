def prime_factorization(n):
    factor = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factor.append(i)
            n //= i
    if n > 1:
        factor.append(n)
    return factor

if __name__ == '__main__':
    prime_factorization()