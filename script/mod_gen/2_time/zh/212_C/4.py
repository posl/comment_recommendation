def getMinDiff(A,B):
    A.sort()
    B.sort()
    minDiff = abs(A[0]-B[0])
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        minDiff = min(minDiff,abs(A[i]-B[j]))
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return minDiff

if __name__ == '__main__':
    getMinDiff()