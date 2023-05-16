def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j - AB[i][1] >= 0 and k - AB[i][0] >= 0:
                    dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j - AB[i][1]][k - AB[i][0]] + 1)
    ans = dp[N][Y][X]
    if ans == float('inf'):
        ans = -1
    print(ans)

if __name__ == '__main__':
    main()