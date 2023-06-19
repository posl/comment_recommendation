def primeFactorization(n):
    primeFactor = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            t = 0
            while n % i == 0:
                n /= i
                t += 1
            primeFactor.append(i ** t)
        i += 1
    if n != 1:
        primeFactor.append(n)
    return primeFactor
N = int(input())
p = primeFactorization(N)
print(len(p))
