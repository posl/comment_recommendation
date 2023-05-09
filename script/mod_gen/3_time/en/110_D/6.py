def get_prime_factors(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 2
    if n != 1:
        prime_factors.append(n)
    return prime_factors

if __name__ == '__main__':
    get_prime_factors()