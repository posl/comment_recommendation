def solve(h, w, k, c):
    # dp[i][j][k] : i行目まで見たときにj個の行を選択し、k個の黒マスになる場合の数
    dp = [[[0 for _ in range(k+1)] for _ in range(w+1)] for _ in range(h+1)]
    dp[0][0][0] = 1
    for i in range(h):
        for j in range(w):
            for l in range(k+1):
                # 何もしない
                dp[i+1][j][l] += dp[i][j][l]
                # 行を選択
                if c[i][j] == "#":
                    dp[i+1][j][l+1] += dp[i][j][l]
                # 列を選択
                dp[i][j+1][l] += dp[i][j][l]
    return dp[h][w][k]
