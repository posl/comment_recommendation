def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    dp = [[0 for _ in range(W)] for _ in range(H)]
    def dfs(i, j, a, b):
        if a < 0 or b < 0:
            return 0
        if j == W:
            j = 0
            i += 1
        if i == H:
            return 1
        if dp[i][j] != 0:
            return dp[i][j]
        res = 0
        #畳を置かない場合
        res += dfs(i, j + 1, a, b)
        if (a > 0):
            #2x1畳を置く場合
            if (j + 1 < W) and (dp[i][j + 1] == 0):
                dp[i][j + 1] = 1
                res += dfs(i, j + 1, a - 1, b)
                dp[i][j + 1] = 0
            #2x2畳を置く場合
            if (i + 1 < H) and (dp[i + 1][j] == 0):
                dp[i + 1][j] = 1
                res += dfs(i, j + 1, a - 1, b - 1)
                dp[i + 1][j] = 0
        if (b > 0):
            #1x1畳を置く場合
            if (dp[i][j] == 0):
                dp[i][j] = 1
                res += dfs(i, j + 1, a, b - 1)
                dp[i][j] = 0
        dp[i][j] = res
        return res
    ans = dfs(0, 0, A, B)
    print(ans)
