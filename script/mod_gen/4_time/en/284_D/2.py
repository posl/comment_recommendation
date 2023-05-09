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
    prime = prime_factors(N)
    p = prime[0]
    q = prime[1]
    print(p, q)

if __name__ == '__main__':
    prime_factors()