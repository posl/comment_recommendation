def solve():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (N+1) for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(N+1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) % MOD
    ans = [0] * (K+1)
    for i in range(1, K+1):
        ans[i] = (dp[i][N] - dp[i][N-i]) % MOD
    for i in range(1, K+1):
        print(ans[i])
solve()

if __name__ == '__main__':
    solve()