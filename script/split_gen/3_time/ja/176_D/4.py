def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = []
    for i in range(H):
        S.append(list(input()))
    #スタート地点とゴール地点の座標を0始まりにする
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    #スタート地点からの距離を記録する
    dist = [[float('inf') for i in range(W)] for j in range(H)]
    dist[C_h][C_w] = 0
    #スタート地点からの距離を更新する
    queue = [[C_h, C_w]]
    while queue:
        h, w = queue.pop(0)
        #移動A
        for dh, dw in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] > dist[h][w]:
                dist[nh][nw] = dist[h][w]
                queue.append([nh, nw])
        #移動B
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] > dist[h][w] + 1:
                    dist[nh][nw] = dist[h][w] + 1
                    queue.append([nh, nw])
    if dist[D_h][D_w] == float('inf'):
        print(-1)
    else:
        print(dist[D_h][D_w])
