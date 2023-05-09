def main():
    n = int(input())
    mod = 10**9+7
    dp = [0]*64
    for i in range(64):
        dp[i] = [0]*64
    dp[0][0] = 1
    for i in range(n):
        for j in range(64):
            for k in range(4):
                if j>>k&1:
                    continue
                nj = (j|1<<k)<<1&63
                if k == 1 and j>>1&1:
                    continue
                if k == 0 and j>>2&1:
                    continue
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= mod
    ans = 0
    for i in range(64):
        ans += dp[n][i]
        ans %= mod
    print(ans)
