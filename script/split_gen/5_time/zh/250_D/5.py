def getPrimeList(N):
    primeList = [2]
    for i in range(3, N+1, 2):
        for j in primeList:
            if i % j == 0:
                break
            elif j > i**0.5:
                primeList.append(i)
                break
    return primeList
