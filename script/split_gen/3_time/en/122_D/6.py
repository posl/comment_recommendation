def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    dp = [[0] * 4 for _ in range(N + 1)]
    for i in range(4):
        dp[1][i] = 1
    for i in range(2, N + 1):
        for j in range(4):
            for k in range(4):
                if j == 0 and k == 2:
                    continue
                if j == 0 and k == 1:
                    continue
                if j == 1 and k == 0:
                    continue
                if j == 2 and k == 0:
                    continue
                dp[i][k] += dp[i - 1][j]
    print(sum(dp[N]) % MOD)
