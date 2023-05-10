def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    # 魔法使いの現在地をキューに入れる
    q = []
    q.append([C_h, C_w])
    # 魔法使いが移動した回数を記録する
    dist = [[-1 for i in range(W)] for j in range(H)]
    dist[C_h][C_w] = 0
    # 移動方向のベクトル
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]
    while len(q) != 0:
        # キューの先頭を取り出す
        h, w = q.pop(0)
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の魔法使いの座標を (nh,nw) とする
            nh = h + dh[i]
            nw = w + dw[i]
            # 移動が可能かの判定と既に訪れたことがあるかの判定 (dist[nh][nw] != -1 なら訪れたことあり)
            if (0 <= nh and nh < H and 0 <= nw and nw < W and S[nh][nw] != '#' and dist[nh][nw] == -1):
                # 移動できるならキューに入れ、その点の距離を更新
                q.append([nh, nw])
                dist[nh][nw] = dist[h][w] + 1
    # 魔法使いが (D_h,D_w) に到達不可能
    if dist[D_h][D_w] == -1:
        print(-1

if __name__ == '__main__':
    main()