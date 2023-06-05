def findMinInt(N, A):
    for i in range(N):
        if A.count(i) == 0:
            return i
    return N
