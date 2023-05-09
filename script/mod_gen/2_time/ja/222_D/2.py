def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0]*3001 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
        for j in range(1, 3001):
            dp[i+1][j] = (dp[i+1][j] + dp[i+1][j-1]) % MOD
    print(dp[N][3000])

if __name__ == '__main__':
    main()