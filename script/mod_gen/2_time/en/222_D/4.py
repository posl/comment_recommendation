def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * 3001 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(B[i]+1):
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % MOD
        for j in range(A[i]+1, B[i]+1):
            dp[i+1][j] = (dp[i+1][j] + dp[i+1][j-1]) % MOD
    print(dp[N][B[N-1]])
solve()
