def main():
    h, w, k = map(int, input().split())
    dp = [[0 for _ in range(w)] for _ in range(h+1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            for k in range(1 << (w-1)):
                ok = True
                for l in range(w-2):
                    if (k >> l) & 1 and (k >> (l+1)) & 1:
                        ok = False
                if not ok:
                    continue
                if j >= 1 and (k >> (j-1)) & 1:
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= mod
                elif j <= w-2 and (k >> j) & 1:
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= mod
                else:
                    dp[i+1][j] += dp[i][j]
                    dp[i+1][j] %= mod
    print(dp[h][k-1])
