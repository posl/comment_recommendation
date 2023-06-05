def getSumList(n):
    sumList = [0]*(n+1)
    sumList[0] = 1
    for i in range(3,n+1):
        for j in range(i,n+1):
            sumList[j] += sumList[j-i]
    return sumList
