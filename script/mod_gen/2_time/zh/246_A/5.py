def getB(n, m, A, C):
    B = [0 for i in range(m + 1)]
    B[0] = C[0] // A[0]
    for i in range(1, m + 1):
        B[i] = (C[i] - sum([B[j] * A[i - j] for j in range(i)])) // A[0]
    return B

if __name__ == '__main__':
    getB()