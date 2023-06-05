def prime_factorization(n):
    factors = []
    for i in range(2, n+1):
        if i * i > n:
            break
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

if __name__ == '__main__':
    prime_factorization()