def calc():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        if S[i].count('#') != T[i].count('#'):
            print('No')
            return
    for j in range(W):
        if [S[i][j] for i in range(H)].count('#') != [T[i][j] for i in range(H)].count('#'):
            print('No')
            return
    print('Yes')
    return
calc()
