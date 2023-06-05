def primeFactorization(n):
    i = 2
    primeList = []
    while i * i <= n:
        if n % i == 0:
            primeList.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        primeList.append(n)
    return primeList
n = int(input())
primeList = primeFactorization(n)
ans = 0
for i in range(1, len(primeList)):
    if primeList[i] != primeList[i - 1]:
        ans += 1
print(ans)

if __name__ == '__main__':
    primeFactorization()