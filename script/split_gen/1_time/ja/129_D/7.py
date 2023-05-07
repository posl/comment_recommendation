def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # print(H, W)
    # print(S)
    # 上下左右の最大値を求める
    # 上
    up = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                up[i][j] = 0
            else:
                if i == 0:
                    up[i][j] = 1
                else:
                    up[i][j] = up[i-1][j] + 1
    # 下
    down = [[0] * W for _ in range(H)]
    for i in range(H-1, -1, -1):
        for j in range(W):
            if S[i][j] == '#':
                down[i][j] = 0
            else:
                if i == H-1:
                    down[i][j] = 1
                else:
                    down[i][j] = down[i+1][j] + 1
    # 左
    left = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                left[i][j] = 0
            else:
                if j == 0:
                    left[i][j] = 1
                else:
                    left[i][j] = left[i][j-1] + 1
    # 右
    right = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W-1, -1, -1):
            if S[i][j] == '#':
                right[i][j] = 0
            else:
                if j == W-1:
                    right[i][j] = 1
                else:
                    right[i][j] = right[i][j+1] + 1
    # print(up)
    # print(down)
    # print(left)
    # print(right)
    # 上下左右の最大値の合計の最大値を求める
    ans = 0
    for i in
