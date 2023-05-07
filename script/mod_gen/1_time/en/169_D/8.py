def getPrimeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n / i
        i = i + 2
    if n > 2:
        factors.append(n)
    return factors
N = int(input())
primeFactors = getPrimeFactors(N)
primeFactors.sort()
count = 1
prev = primeFactors[0]
for i in range(1, len(primeFactors)):
    if primeFactors[i] != prev:
        count += 1
        prev = primeFactors[i]
print(count)

if __name__ == '__main__':
    getPrimeFactors()