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
T = int(input())
for i in range(T):
    N = int(input())
    factors = prime_factors(N)
    if len(factors) == 3:
        print(factors[0], factors[1]*factors[2])
    else:
        print(factors[0]*factors[1], factors[2])
