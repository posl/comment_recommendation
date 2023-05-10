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
n = int(input())
factors = prime_factors(n)
factors = list(set(factors))
count = 0
for i in factors:
    tmp = n
    while tmp % i == 0:
        count += 1
        tmp /= i
print(count)
