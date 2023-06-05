def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0 for i in range(3001)] for j in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(A[i-1], B[i-1]+1):
            dp[i][j] = dp[i-1][j]
        for j in range(1, 3001):
            dp[i][j] += dp[i][j-1]
            dp[i][j] %= MOD
    print(dp[N][3000])
solve()
