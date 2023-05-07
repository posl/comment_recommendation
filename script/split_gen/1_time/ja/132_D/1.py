def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(1, N+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) % mod
    for i in range(1, K+1):
        print((dp[i][N] - dp[i-1][N]) % mod)
