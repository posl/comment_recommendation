def solve():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(1, M+1):
                if j+k <= K:
                    dp[i][j+k] += dp[i-1][j]
                    dp[i][j+k] %= mod
    print(dp[N][K])
solve()

if __name__ == '__main__':
    solve()