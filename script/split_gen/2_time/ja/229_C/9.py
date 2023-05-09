def solve():
    N, W = map(int, input().split())
    max_A = 10**9
    max_B = 1000
    # dp[i][j] := i番目までのチーズを使って重さjを作るときのチーズのおいしさの最大値
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        a, b = map(int, input().split())
        for j in range(W+1):
            if j - b >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-b] + a)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][W])
