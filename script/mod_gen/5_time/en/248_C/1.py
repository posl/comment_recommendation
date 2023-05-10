def solve(N, M, K):
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                for l in range(j, M+1):
                    if k + l <= K:
                        dp[i+1][l][k+l] += dp[i][j][k]
                        dp[i+1][l][k+l] %= 998244353
    return sum(dp[N][j][K] for j in range(M+1)) % 998244353
N, M, K = map(int, input().split())
print(solve(N, M, K))

if __name__ == '__main__':
    solve()