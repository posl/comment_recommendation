def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    # print(H, W)
    # print(C_h, C_w)
    # print(D_h, D_w)
    # print(S)
    # 0: 壁
    # 1: 道
    # 2: 魔法使いの位置
    # 3: 目的地の位置
    # 4: 未訪問
    # 5: 訪問済み
    S_ = [[0 if S[i][j] == "#" else 1 for j in range(W)] for i in range(H)]
    S_[C_h][C_w] = 2
    S_[D_h][D_w] = 3
    # print(S_)
    # 0: 壁
    # 1: 道
    # 2: 魔法使いの位置
    # 3: 目的地の位置
    # 4: 未訪問
    # 5: 訪問済み
    # 6: ワープ魔法で訪問済み
    S_warp = [[0 if S[i][j] == "#" else 1 for j in range(W)] for i in range(H)]
    S_warp[C_h][C_w] = 2
    S_warp[D_h][D_w] = 3
    # print(S_warp)
    # 移動A
    # 移動B
    # 4: 未訪問
    # 5: 訪問済み
    # 6: ワープ魔法で訪問済み
    # 7: ワープ魔法で訪問済み(5x5範囲内)
    # 8: ワープ魔法で訪

if __name__ == '__main__':
    main()