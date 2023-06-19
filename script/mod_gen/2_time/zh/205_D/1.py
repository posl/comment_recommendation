def getKthNumber(A, K):
    if len(A) == 0:
        return K
    if K == 0:
        return 0
    if K == 1:
        return A[0] + 1
    if K == 2:
        return A[0] * 2
    if K == 3:
        return A[0] * 2 + 1
    if K == 4:
        return A[0] * 4
    if K == 5:
        return A[0] * 4 + 1
    if K == 6:
        return A[0] * 4 + 2
    if K == 7:
        return A[0] * 4 + 3
    if K == 8:
        return A[0] * 8
    if K == 9:
        return A[0] * 8 + 1
    if K == 10:
        return A[0] * 8 + 2
    if K == 11:
        return A[0] * 8 + 3
    if K == 12:
        return A[0] * 8 + 4
    if K == 13:
        return A[0] * 8 + 5
    if K == 14:
        return A[0] * 8 + 6
    if K == 15:
        return A[0] * 8 + 7
    if K == 16:
        return A[0] * 16
    if K == 17:
        return A[0] * 16 + 1
    if K == 18:
        return A[0] * 16 + 2
    if K == 19:
        return A[0] * 16 + 3
    if K == 20:
        return A[0] * 16 + 4
    if K == 21:
        return A[0] * 16 + 5
    if K == 22:
        return A[0] * 16 + 6
    if K == 23:
        return A[0] * 16 + 7
    if K == 24:
        return A[0] * 16 + 8
    if

if __name__ == '__main__':
    getKthNumber()