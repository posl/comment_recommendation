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
t=int(input())
for i in range(t):
    n=int(input())
    x=prime_factors(n)
    a=x[0]
    b=x[1]
    print(a,b)
