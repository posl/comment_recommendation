def findMinNonNegInt(A):
    A.sort()
    N = len(A)
    if A[0] > 0:
        return 0
    if A[N-1] <= 0:
        return 1
    for i in range(N-1):
        if A[i] < 0 and A[i+1] > 0:
            if A[i+1] > 1:
                return 1
            else:
                continue
        if A[i] >= 0 and A[i+1] - A[i] > 1:
            return A[i] + 1
    return A[N-1] + 1
