def getMinTime(n:int, snukeTimes:list, takaTimes:list):
    minTime = [0]*n
    for i in range(n):
        minTime[i] = min(takaTimes[i], snukeTimes[i])
    return minTime

if __name__ == '__main__':
    getMinTime()