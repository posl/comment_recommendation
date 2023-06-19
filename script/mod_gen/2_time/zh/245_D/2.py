def getB():
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    N = len(A) - 1
    M = len(C) - 1
    B = [0 for _ in range(M+1)]
    for i in range(M, N-1, -1):
        B[i-N] = C[i] // A[N]
        for j in range(N, -1, -1):
            C[i-N+j] -= A[j] * B[i-N]
    for i in range(M, N-1, -1):
        if C[i] != 0:
            return False
    return B

if __name__ == '__main__':
    getB()