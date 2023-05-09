def main():
    N,M,K = map(int, input().split())
    MOD = 998244353
    ans = 0
    # i個目までの数列の総和をjとする
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(K+1):
            for k in range(1,M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= MOD
    print(dp[N][K])
