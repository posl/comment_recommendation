def getPrime(n):
    primeList = []
    for i in range(2, n + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
        if isPrime:
            primeList.append(i)
    return primeList

if __name__ == '__main__':
    getPrime()