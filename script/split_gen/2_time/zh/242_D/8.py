def main():
    N = int(input())
    dp = [[0] * 10 for _ in range(N + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, N + 1):
        for j in range(10):
            for k in range(10):
                if abs(j - k) <= 1:
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= 998244353
    print(sum(dp[N]) % 998244353)
