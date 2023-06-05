def findMinNonNegativeInteger(N, A):
    A.sort()
    maxNum = A[-1]
    if maxNum == 0:
        return 0
    for i in range(maxNum):
        if i not in A:
            return i
    return maxNum + 1
