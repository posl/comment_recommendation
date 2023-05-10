def findSum(S, N, A, B):
    for i in range(N):
        if A[i] >= S:
            return i, 'F'
        if B[i] >= S:
            return i, 'B'
    return -1, 'F'

if __name__ == '__main__':
    findSum()