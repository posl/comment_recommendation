def getPrimeList(x):
    primeList = []
    for i in range(2, x):
        if isPrime(i):
            primeList.append(i)
    return primeList

if __name__ == '__main__':
    getPrimeList()