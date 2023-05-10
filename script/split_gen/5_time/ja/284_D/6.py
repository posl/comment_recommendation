def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors
T = int(input())
for i in range(T):
    N = int(input())
    factors = get_prime_factors(N)
    p = factors[0]
    q = factors[1]
    print("{} {}".format(p, q))
