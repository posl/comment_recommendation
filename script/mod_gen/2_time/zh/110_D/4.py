def getPrimeList(n):
    primeList = []
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, n + 1):
        if isPrime[i]:
            primeList.append(i)
            for j in range(i * 2, n + 1, i):
                isPrime[j] = False
    return primeList

if __name__ == '__main__':
    getPrimeList()