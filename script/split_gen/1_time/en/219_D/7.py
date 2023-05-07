def main():
    n = int(input())
    x, y = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    dp = [[[float('inf')] * (x+1) for _ in range(y+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(y+1):
            for k in range(x+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                if j+b[i] <= y:
                    dp[i+1][j+b[i]][k] = min(dp[i+1][j+b[i]][k], dp[i][j][k]+1)
                if k+a[i] <= x:
                    dp[i+1][j][k+a[i]] = min(dp[i+1][j][k+a[i]], dp[i][j][k]+1)
    ans = min(dp[n][y][x], dp[n][x][y])
    if ans == float('inf'):
        ans = -1
    print(ans)
