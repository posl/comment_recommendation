def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S_count = [[0] * W for _ in range(H)]
    T_count = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                S_count[i][j] = 1
            if T[i][j] == '#':
                T_count[i][j] = 1
    for i in range(H):
        for j in range(1, W):
            S_count[i][j] += S_count[i][j - 1]
            T_count[i][j] += T_count[i][j - 1]
    for i in range(1, H):
        for j in range(W):
            S_count[i][j] += S_count[i - 1][j]
            T_count[i][j] += T_count[i - 1][j]
    for i in range(H):
        for j in range(W):
            if S_count[i][j] != T_count[i][j]:
                print('No')
                return
    print('Yes')
