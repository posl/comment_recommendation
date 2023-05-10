def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [[-float('inf')]*(M+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M+1):
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + A[i]*(i-j+1))
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    print(dp[N][M])
