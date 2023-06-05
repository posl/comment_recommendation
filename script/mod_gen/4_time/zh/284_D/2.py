def getPrimeList(n):
    primeList = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primeList.append(i)
    return primeList

if __name__ == '__main__':
    getPrimeList()