def findMinNonNegativeInteger(A):
    A.sort()
    if A[0] != 0:
        return 0
    for i in range(len(A)-1):
        if A[i+1] - A[i] > 1:
            return A[i] + 1
    return A[len(A)-1] + 1
