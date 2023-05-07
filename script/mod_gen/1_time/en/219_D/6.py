def main():
    n = int(input())
    x, y = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    dp = [[[float('inf')] * (x + y + 1) for _ in range(y + 1)] for _ in range(x + 1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x + 1):
            for k in range(y + 1):
                dp[j][k][a[i]] = min(dp[j][k][a[i]], dp[j][k][0] + 1)
                dp[j][k][b[i]] = min(dp[j][k][b[i]], dp[j][k][0] + 1)
                if j >= a[i]:
                    dp[j][k][j + b[i]] = min(dp[j][k][j + b[i]], dp[j][k][j] + 1)
                if k >= b[i]:
                    dp[j][k][j + a[i]] = min(dp[j][k][j + a[i]], dp[j][k][k] + 1)
    ans = float('inf')
    for i in range(x, x + y + 1):
        ans = min(ans, dp[x][y][i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()