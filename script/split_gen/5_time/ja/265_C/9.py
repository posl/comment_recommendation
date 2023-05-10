def solve():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    # 4方向の移動
    dx = [0, 1, 0, -1]  # 右,下,左,上
    dy = [1, 0, -1, 0]
    # スタート地点
    x, y = 0, 0
    # スタート地点の移動方向
    d = 0
    # 移動できるかどうか
    move = True
    # 移動できなくなるまで繰り返す
    while move:
        # 移動できるかどうかのフラグをFalseにしておく
        move = False
        # 移動方向に移動できるかどうか
        if 0 <= x + dx[d] < W and 0 <= y + dy[d] < H and G[y + dy[d]][x + dx[d]] != "#":
            x += dx[d]
            y += dy[d]
            move = True
        else:
            # 移動できなければ右に回転する
            d = (d + 1) % 4
    # 答えを出力
    print(y + 1, x + 1)
