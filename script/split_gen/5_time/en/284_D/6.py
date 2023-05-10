def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(int(i))
    if n > 1:
        factors.append(int(n))
    return factors
T = int(input())
for i in range(T):
    N = int(input())
    factors = primeFactors(N)
    p = factors[0]
    q = factors[1]
    print(p,q)
