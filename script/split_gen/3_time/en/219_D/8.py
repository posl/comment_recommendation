def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf')] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + Y + 1):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            if j + AB[i][0] <= X + Y:
                dp[i + 1][j + AB[i][0]] = min(dp[i + 1][j + AB[i][0]], dp[i][j] + AB[i][1])
            if j + AB[i][1] <= X + Y:
                dp[i + 1][j + AB[i][1]] = min(dp[i + 1][j + AB[i][1]], dp[i][j] + AB[i][0])
    ans = float('inf')
    for i in range(X, X + Y + 1):
        ans = min(ans, dp[N][i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
