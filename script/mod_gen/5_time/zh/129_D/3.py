def solve():
    # 读取输入
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    # 从左往右，从上往下，分别统计到达每个格子的光线的最远距离
    # 从右往左，从下往上，分别统计到达每个格子的光线的最远距离
    # 然后将两个方向的光线长度求和，即为放置灯照亮的格子数
    # 这里的光线长度是指光线能够到达的最远距离，包括光线发出的格子
    L = [[0] * W for _ in range(H)]
    R = [[0] * W for _ in range(H)]
    U = [[0] * W for _ in range(H)]
    D = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            if j == 0:
                L[i][j] = 1
            else:
                L[i][j] = L[i][j - 1] + 1
            if i == 0:
                U[i][j] = 1
            else:
                U[i][j] = U[i - 1][j] + 1
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if S[i][j] == '#':
                continue
            if j == W - 1:
                R[i][j] = 1
            else:
                R[i][j] = R[i][j + 1] + 1
            if i == H - 1:
                D[i][j] = 1
            else:
                D[i][j] = D[i + 1][j] + 1
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, L

if __name__ == '__main__':
    solve()