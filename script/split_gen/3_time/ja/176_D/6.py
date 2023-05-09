def main():
    # 入力
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    # 0-indexed
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    # 移動Aを行う場合の最短距離
    distA = [[-1] * W for _ in range(H)]
    distA[C_h][C_w] = 0
    # 移動Aを行うためのキュー
    queA = [(C_h, C_w)]
    # 移動Aを行う
    while queA:
        h, w = queA.pop(0)
        # 上下左右に移動
        for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nh = h + dh
            nw = w + dw
            # 移動先が迷路の外に出る場合は無視
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            # 移動先が壁の場合は無視
            if S[nh][nw] == "#":
                continue
            # 移動先がすでに訪問済みの場合は無視
            if distA[nh][nw] != -1:
                continue
            # 移動先の距離を更新
            distA[nh][nw] = distA[h][w] + 1
            # キューに追加
            queA.append((nh, nw))
    # 移動Bを行う場合の最短距離
    distB = [[-1] * W for _ in range(H)]
    distB[C_h][C_w] = 0
    # 移動Bを行うためのキュー
    queB = [(C_h, C_w)]
    #
