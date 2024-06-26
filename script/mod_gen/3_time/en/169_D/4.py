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
print(len(set(factors)))

if __name__ == '__main__':
    prime_factors()