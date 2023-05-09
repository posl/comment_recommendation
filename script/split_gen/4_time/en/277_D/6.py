def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = []
    for i in range(N):
        if i == 0:
            B.append(A[i])
        else:
            if A[i] != B[-1]:
                B.append(A[i])
    N = len(B)
    if N == 1:
        return 0
    if N == 2:
        if (B[1] - B[0]) % M == 1:
            return 0
        else:
            return B[0] + B[1]
    if N == 3:
        if (B[1] - B[0]) % M == 1 and (B[2] - B[1]) % M == 1:
            return 0
        if (B[1] - B[0]) % M == 1:
            return B[2]
        if (B[2] - B[1]) % M == 1:
            return B[0]
        return B[0] + B[1] + B[2]
    if N == 4:
        if (B[1] - B[0]) % M == 1 and (B[2] - B[1]) % M == 1 and (B[3] - B[2]) % M == 1:
            return 0
        if (B[1] - B[0]) % M == 1 and (B[2] - B[1]) % M == 1:
            return B[3]
        if (B[2] - B[1]) % M == 1 and (B[3] - B[2]) % M == 1:
            return B[0]
        if (B[1] - B[0]) % M == 1 and (B[3] - B[2]) % M == 1:
            return B[2]
        if (B[1] - B[0]) % M == 1:
            return B[2] + B[3]
        if (B[2] - B[1]) % M == 1:
            return B[0] + B[3]
        if (B[3] - B[2]) % M == 1:
