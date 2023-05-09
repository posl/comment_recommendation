def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0]*(N+1) for _ in range(K+1)]
    dp[0][0] = 1
    for k in range(K):
        for n in range(N):
            dp[k+1][n+1] = (dp[k+1][n] + dp[k][n])%MOD
    for k in range(1, K+1):
        ans = 0
        for n in range(N, N-K+k-1, -1):
            ans = (ans + dp[k][n])%MOD
        print(ans)

if __name__ == '__main__':
    main()