def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
t = int(input())
for i in range(t):
    n = int(input())
    factors = prime_factors(n)
    p = factors[0]
    q = factors[1]
    print(p, q)

if __name__ == '__main__':
    prime_factors()