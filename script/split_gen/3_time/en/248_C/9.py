def main():
    import sys
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(1, M + 1):
        dp[1][i] = 1
    for i in range(2, N + 1):
        for j in range(1, K + 1):
            for k in range(1, M + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
                    dp[i][j] %= MOD
    print(dp[-1][-1])
