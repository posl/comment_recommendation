def findSecondPlace(N, A):
    A = sorted(A)
    A.reverse()
    A.pop(0)
    A.pop(0)
    A.reverse()
    return A[0]
