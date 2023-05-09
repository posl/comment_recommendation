def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    INF = 10 ** 10
    # 魔法使用回数
    magic = [[INF] * W for _ in range(H)]
    magic[C_h][C_w] = 0
    # 移動可能かどうか
    can_move = [[False] * W for _ in range(H)]
    can_move[C_h][C_w] = True
    # 移動可能なマスを探索するキュー
    que = [(C_h, C_w)]
    while que:
        h, w = que.pop(0)
        # 移動可能なマスを探索
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == ".":
                if not can_move[nh][nw]:
                    can_move[nh][nw] = True
                    que.append((nh, nw))
    # 周囲5マスを探索
    for h in range(H):
        for w in range(W):
            if not can_move[h][w]:
                continue
            for dh in range(-2, 3):
                for dw in range(-2, 3):
                    nh = h + dh
                    nw = w + dw
                    if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == ".":
                        can_move[nh][nw] = True
    # 移動可能なマスを探索するキュー
    que = [(C_h, C_w)]
    while que:
        h, w = que.pop(0)
        # 移動可能なマスを探索
        for dh, dw in ((1, 0),

if __name__ == '__main__':
    main()