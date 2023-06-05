def rotate90(S):
    N = len(S)
    S2 = [['' for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            S2[N-1-j][i] = S[i][j]
    return S2
