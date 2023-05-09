def solve():
    N, W = map(int, input().split())
    # dp[i][j] := i番目までのチーズで重さがjになるようにしたときのおいしさの最大値
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(W+1):
            if j - a >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-a] + b)
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])
