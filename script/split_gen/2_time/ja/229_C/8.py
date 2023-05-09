def main():
    N, W = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # dp[i][j] := i番目までのチーズで重さjの時の最大のおいしさ
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i]] + B[i])
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= AB[i][0]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-AB[i][0]] + AB[i][1])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])
