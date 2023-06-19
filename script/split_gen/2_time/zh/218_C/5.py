def rotate90(S):
    N = len(S)
    T = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            T[i][j] = S[N-1-j][i]
    return T
