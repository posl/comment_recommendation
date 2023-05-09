def main():
    N = int(input())
    MOD = 998244353
    # dp[i][j][k] := i 桁目まで見て、j で終わる数列の個数
    # k = 0: 両隣の差が 1 以下
    # k = 1: 両隣の差が 1
    # k = 2: 両隣の差が 2
    dp = [[[0] * 3 for _ in range(10)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(10):
            for k in range(3):
                for d in range(10):
                    if abs(j - d) <= 1:
                        dp[i + 1][d][1 if k == 0 and abs(j - d) == 1 else k] += dp[i][j][k]
                        dp[i + 1][d][1 if k == 0 and abs(j - d) == 1 else k] %= MOD
    ans = 0
    for j in range(1, 10):
        ans += sum(dp[N][j])
        ans %= MOD
    print(ans)
