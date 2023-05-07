def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 上から見たときの照らされるマスの個数
    up = [[0] * W for _ in range(H)]
    # 下から見たときの照らされるマスの個数
    down = [[0] * W for _ in range(H)]
    # 左から見たときの照らされるマスの個数
    left = [[0] * W for _ in range(H)]
    # 右から見たときの照らされるマスの個数
    right = [[0] * W for _ in range(H)]
    # 上から見たときの照らされるマスの個数を求める
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                continue
            # 一番上の行の場合
            if h == 0:
                up[h][w] = 1
            else:
                up[h][w] = up[h-1][w] + 1
    # 下から見たときの照らされるマスの個数を求める
    for h in range(H - 1, -1, -1):
        for w in range(W):
            if S[h][w] == "#":
                continue
            # 一番下の行の場合
            if h == H - 1:
                down[h][w] = 1
            else:
                down[h][w] = down[h+1][w] + 1
    # 左から見たときの照らされるマスの個数を求める
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                continue
            # 一番左の列の場合
            if w == 0:
                left[h][w] = 1
            else:
                left[h][w] = left[h][w-1] + 1
    # 右から見たときの照らされ
