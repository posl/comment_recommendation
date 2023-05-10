def main():
    H, W, K = map(int, input().split())
    dp = [[0 for _ in range(W)] for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            for k in range(1 << (W - 1)):
                ok = True
                for l in range(W - 2):
                    if (k >> l) & 1 and (k >> (l + 1)) & 1:
                        ok = False
                        break
                if not ok:
                    continue
                if j >= 1 and (k >> (j - 1)) & 1:
                    dp[i + 1][j - 1] += dp[i][j]
                    dp[i + 1][j - 1] %= 1000000007
                elif j <= W - 2 and (k >> j) & 1:
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= 1000000007
                else:
                    dp[i + 1][j] += dp[i][j]
                    dp[i + 1][j] %= 1000000007
    print(dp[H][K - 1])
