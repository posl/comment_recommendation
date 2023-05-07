def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 上から見たときの照らされるマスの数
    dp1 = [[0] * W for _ in range(H)]
    # 左から見たときの照らされるマスの数
    dp2 = [[0] * W for _ in range(H)]
    # 上から見たときの照らされるマスの数を求める
    for i in range(H):
        cnt = 0
        for j in range(W):
            if S[i][j] == "#":
                cnt = 0
            else:
                cnt += 1
            dp1[i][j] = cnt
    # 左から見たときの照らされるマスの数を求める
    for j in range(W):
        cnt = 0
        for i in range(H):
            if S[i][j] == "#":
                cnt = 0
            else:
                cnt += 1
            dp2[i][j] = cnt
    # 照らされるマスの数の最大値を求める
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            ans = max(ans, dp1[i][j] + dp2[i][j] - 1)
    print(ans)
