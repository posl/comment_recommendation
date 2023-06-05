def solve(N,M,K):
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1,M+1):
        dp[1][i][i] = 1
    for i in range(2,N+1):
        for j in range(1,M+1):
            for k in range(1,K+1):
                if k-j>=0:
                    dp[i][j][k] = sum(dp[i-1][j][k-j:])
    return sum(dp[N][j][K] for j in range(1,M+1))%(998244353)
N,M,K = map(int, input().split())
print(solve(N,M,K))
