def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(0, N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[0 for i in range(0, Y + 1)] for j in range(0, X + 1)] for k in range(0, N + 1)]
    for n in range(1, N + 1):
        for x in range(0, X + 1):
            for y in range(0, Y + 1):
                dp[n][x][y] = min(dp[n][x][y], dp[n - 1][x][y])
                if x >= A[n - 1]:
                    dp[n][x][y] = min(dp[n][x][y], dp[n - 1][x - A[n - 1]][y] + 1)
                if y >= B[n - 1]:
                    dp[n][x][y] = min(dp[n][x][y], dp[n - 1][x][y - B[n - 1]] + 1)
    if dp[N][X][Y] == 10 ** 10:
        print(-1)
    else:
        print(dp[N][X][Y])

if __name__ == '__main__':
    main()