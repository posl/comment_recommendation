def main():
    #入力
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    C_h -= 1
    C_w -= 1
    D_h,D_w = map(int,input().split())
    D_h -= 1
    D_w -= 1
    S = []
    for i in range(H):
        S.append(list(input()))
    #print(H,W,C_h,C_w,D_h,D_w,S)
    #移動可能かどうか
    if S[D_h][D_w] == "#":
        print(-1)
        return
    #移動可能なマスを保存
    S[C_h][C_w] = 0
    S[D_h][D_w] = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                S[i][j] = -1
    #移動可能なマスを保存
    #print(S)
    for i in range(H):
        for j in range(W):
            if S[i][j] == 0:
                #print(i,j)
                for k in range(-2,3):
                    for l in range(-2,3):
                        if 0 <= i+k < H and 0 <= j+l < W and S[i+k][j+l] != "#":
                            if abs(k) + abs(l) == 1:
                                S[i+k][j+l] = 0
                            else:
                                S[i+k][j+l] = 1
    #print(S)
    #print(S[D_h][D_w])
    if S[D_h][D_w] == -1:
        print(-1)
        return
    #移動可能なマスを保存
    #print(S)
    for i in range(H):
        for j in range(W):
            if S[i][j] == 0:
                #print(i,j)
                for k in range(-2,3):
                    for l in range(-2,3):
                        if 0 <= i+k < H and 0 <= j+l < W and S[i+k][j+l] != "#":
                            if abs(k) + abs(l) == 1:
                                S[i+k][j+l] = 0
                            else:
                                S[i+k][j

if __name__ == '__main__':
    main()