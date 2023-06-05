def rotate90(S):
    N = len(S)
    T = [['' for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            T[j][N-1-i] = S[i][j]
    return T
