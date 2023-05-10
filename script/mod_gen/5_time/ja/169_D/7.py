def prime_factorize(n):
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
N = int(input())
prime_factors = prime_factorize(N)
prime_factors.sort()
ans = 0

if __name__ == '__main__':
    prime_factorize()