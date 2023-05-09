def findPairs(A, B, C):
    count = 0
    for i in range(len(A)):
        if A[i] == B[C[i] - 1]:
            count += 1
    return count
