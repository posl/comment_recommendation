def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float("inf")] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + Y + 1):
            if j < AB[i][0] + AB[i][1]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - AB[i][0] - AB[i][1]] + 1)
    if dp[N][X + Y] == float("inf"):
        print(-1)
    else:
        print(dp[N][X + Y])

if __name__ == '__main__':
    main()