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
for i in range(0,t):
    n = int(input())
    p = prime_factors(n)
    q = int(n/(p[0]*p[0]))
    print(p[0],q)

if __name__ == '__main__':
    prime_factors()