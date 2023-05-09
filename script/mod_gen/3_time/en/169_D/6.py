def prime_factorize(n):
    if n == 1:
        return []
    factor = []
    while n % 2 == 0:
        factor.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            factor.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        factor.append(n)
    return factor
n = int(input())
factor = prime_factorize(n)
factor.sort()
length = len(factor)

if __name__ == '__main__':
    prime_factorize()