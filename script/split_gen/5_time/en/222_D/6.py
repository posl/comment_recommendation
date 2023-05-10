def solve(N, A, B):
    dp = [[0 for _ in range(3001)] for _ in range(N)]
    for i in range(A[0], B[0]+1):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(A[i], B[i]+1):
            dp[i][j] = sum(dp[i-1][:j+1]) % 998244353
    return sum(dp[N-1]) % 998244353
