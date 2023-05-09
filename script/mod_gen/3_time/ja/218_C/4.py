def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    T = [list(input()) for _ in range(N)]
    # Sの連結成分を求める
    S_connected = []
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                S_connected.append([i,j])
    # Tの連結成分を求める
    T_connected = []
    for i in range(N):
        for j in range(N):
            if T[i][j] == '#':
                T_connected.append([i,j])
    # SとTの連結成分の数が違うならNo
    if len(S_connected) != len(T_connected):
        print('No')
        return
    # Sの連結成分を原点に移動
    S_connected = [[x-S_connected[0][0],y-S_connected[0][1]] for x,y in S_connected]
    # Tの連結成分を原点に移動
    T_connected = [[x-T_connected[0][0],y-T_connected[0][1]] for x,y in T_connected]
    # Tの連結成分を90度回転
    T_connected_rotate = [[y,-x] for x,y in T_connected]
    # SとTの連結成分を90度回転
    T_connected_rotate = [[y,-x] for x,y in T_connected]
    # Sの連結成分を原点に移動
    T_connected_rotate = [[x-T_connected_rotate[0][0],y-T_connected_rotate[0][1]] for x,y in T_connected_rotate]
    # SとTの連結成分を90度回転
    T_connected_rotate = [[y,-x] for x,y in T_connected_rotate]
    # Sの連結成分を原点に移動
    T_connected_rotate = [[x-T_connected_rotate[0][0],y-T_connected_rotate[0][1]] for x,y in T_connected_rotate]
    # SとTの連結成分を90度回転
    T_connected_rotate = [[y,-x] for x,y in

if __name__ == '__main__':
    main()