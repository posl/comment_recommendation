def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[float("inf")] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + AB[i][0] <= X and k + AB[i][1] <= Y:
                    dp[i + 1][j + AB[i][0]][k + AB[i][1]] = min(dp[i + 1][j + AB[i][0]][k + AB[i][1]], dp[i][j][k] + 1)
    print(-1 if dp[N][X][Y] == float("inf") else dp[N][X][Y])

if __name__ == '__main__':
    main()