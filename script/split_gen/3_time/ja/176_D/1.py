def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    # ワープ魔法の範囲
    warp_range = 2
    # ワープ魔法の範囲を考慮した迷路
    warp_S = [['#' for _ in range(W + warp_range * 2)] for _ in range(H + warp_range * 2)]
    # ワープ魔法の範囲を考慮した現在地
    warp_C_h = C_h + warp_range
    warp_C_w = C_w + warp_range
    # ワープ魔法の範囲を考慮したゴール
    warp_D_h = D_h + warp_range
    warp_D_w = D_w + warp_range
    # ワープ魔法の範囲を考慮した迷路を作成
    for i in range(H):
        for j in range(W):
            warp_S[i + warp_range][j + warp_range] = S[i][j]
    # 移動可能な座標を格納するリスト
    movable = []
    # 移動可能な座標を追加
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                movable.append((i, j))
    # 移動可能な座標の数
    movable_num = len(movable)
    # 移動可能な座標に対応するワープ魔法の使用回数を格納するリスト
    warp_num = [-1 for _ in range(movable_num)]
    # ワープ魔法の使用回数を計算
    for i in range(movable_num):
        warp_num[i] = abs(movable
