def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K+1):
            if j > 0:
                dp[i+1][j] += dp[i][j-1]
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
    ans = [0]*K
    for i in range(1, K+1):
        ans[i-1] = dp[N][i] * dp[N-K][K-i]
        ans[i-1] %= mod
    print('
'.join(map(str, ans)))
