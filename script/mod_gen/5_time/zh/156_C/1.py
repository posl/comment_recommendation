def findMinSum(xList):
    xList.sort()
    minSum = 0
    for x in xList:
        minSum += (x-xList[0])**2
    return minSum

if __name__ == '__main__':
    findMinSum()