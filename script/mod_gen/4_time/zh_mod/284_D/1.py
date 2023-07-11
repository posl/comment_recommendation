def getPrimeList(num):
    primeList = []
    for i in range(2,num+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:

if __name__ == '__main__':
    getPrimeList()