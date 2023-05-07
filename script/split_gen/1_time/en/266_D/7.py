def solve():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    S.sort()
    dp = [[0] * 5 for _ in range(N+1)]
    for i in range(N):
        t, x, a = S[i]
        for j in range(5):
            if j == x:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + a if j > 0 else 0)
                dp[i+1][j] = max(dp[i+1][j], dp[i][j+1] + a if j < 4 else 0)
            else:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    print(max(dp[N]))
