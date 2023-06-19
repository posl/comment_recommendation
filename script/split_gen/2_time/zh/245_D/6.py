def getB(A,C):
    N = len(A) - 1
    M = len(C) - 1
    B = [0]*(M+1)
    for i in range(N+1):
        for j in range(M+1):
            B[j] += A[i]*C[j-i]
    return B
