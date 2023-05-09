def findPrimeFactors(n):
    factors = []
    i = 2
    while i*i <= n:
        if n%i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
t = int(input())
for _ in range(t):
    n = int(input())
    factors = findPrimeFactors(n)
    if len(set(factors)) == 2:
        p = factors[0]
        q = factors[1]
        print(p, q)
    else:
        print(0, 0)

if __name__ == '__main__':
    findPrimeFactors()