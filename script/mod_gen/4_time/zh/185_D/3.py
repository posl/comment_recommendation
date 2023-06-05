def stamp(N, M, A):
    if M == 0:
        return 1
    A.sort()
    B = []
    for i in range(M):
        if i == 0:
            B.append(A[i] - 1)
        else:
            B.append(A[i] - A[i-1] - 1)
    B.append(N - A[M-1])
    if M == 1:
        return B[0]
    C = []
    for i in range(M):
        if i == 0:
            C.append(B[i] + B[i+1])
        elif i == M-1:
            C.append(B[i-1] + B[i])
        else:
            C.append(B[i-1] + B[i] + B[i+1])
    return min(C)

if __name__ == '__main__':
    stamp()