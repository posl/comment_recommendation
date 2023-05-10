def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    p = [0]*(N+1)
    for i in range(N):
        p[i+1] = min(B[i], p[i]+1)
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N+1):
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
            if A[i] <= j <= p[i+1]:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
    print(dp[N][N])

if __name__ == '__main__':
    main()