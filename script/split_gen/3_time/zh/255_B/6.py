def getMinLight(L, A):
    minLight = 0
    for i in range(len(A)):
        minLight = max(minLight, L[A[i]-1])
    return minLight
