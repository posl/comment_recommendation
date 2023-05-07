def main():
    N = int(input())
    S = [[0 for _ in range(N)] for _ in range(N)]
    T = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        S[i] = list(input())
    for i in range(N):
        T[i] = list(input())
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                S[i][j] = 1
            else:
                S[i][j] = 0
    for i in range(N):
        for j in range(N):
            if T[i][j] == '#':
                T[i][j] = 1
            else:
                T[i][j] = 0
    #S,Tの最上段の左端の座標を格納
    S_x = 0
    S_y = 0
    T_x = 0
    T_y = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                S_x = i
                S_y = j
                break
    for i in range(N):
        for j in range(N):
            if T[i][j] == 1:
                T_x = i
                T_y = j
                break
    #TをSに合わせる
    for i in range(N):
        for j in range(N):
            T[i][j] = T[i][j] ^ S[S_x - T_x + i][S_y - T_y + j]
    #Tが全て0かどうかを確認
    for i in range(N):
        for j in range(N):
            if T[i][j] == 1:
                print('No')
                return
    print('Yes')
