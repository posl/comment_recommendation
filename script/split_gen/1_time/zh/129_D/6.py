def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    # 縦方向に障害物があるかどうかを判定
    # あるならその位置までの距離を記録
    # ないなら-1を記録
    # dp[i][j] = (i, j)から上方向にある障害物までの距離
    dp = [[0] * W for i in range(H)]
    for j in range(W):
        for i in range(H):
            if S[i][j] == "#":
                dp[i][j] = -1
            elif i > 0:
                dp[i][j] = dp[i - 1][j] + 1
    # 横方向に障害物があるかどうかを判定
    # あるならその位置までの距離を記録
    # ないなら-1を記録
    # dp[i][j] = (i, j)から左方向にある障害物までの距離
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                dp[i][j] = -1
            elif j > 0:
                dp[i][j] += dp[i][j - 1]
    # 縦方向に障害物があるかどうかを判定
    # あるならその位置までの距離を記録
    # ないなら-1を記録
    # dp[i][j] = (i, j)から下方向にある障害物までの距離
    for j in range(W):
        for i in range(H - 1, -1, -1):
            if S[i][j] == "#":
                dp[i][j] = -1
            elif i < H - 1:
                dp[i][j] += dp[i + 1][
