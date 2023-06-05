def getPrimeList(n):
    primeList = [2]
    for i in range(3,n+1,2):
        for j in primeList:
            if i % j == 0:
                break
        else:
            primeList.append(i)
    return primeList

if __name__ == '__main__':
    getPrimeList()