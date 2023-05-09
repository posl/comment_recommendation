def getNumOfWays(L):
    if L == 12:
        return 1
    else:
        return 12 * getNumOfWays(L - 1) + 1
L = int(input())
print(getNumOfWays(L))

if __name__ == '__main__':
    getNumOfWays()