def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[0] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    for n in range(1, N + 1):
        for y in range(Y + 1):
            for x in range(X + 1):
                a, b = AB[n - 1]
                dp[n][y][x] = dp[n - 1][y][x]
                if y >= b:
                    dp[n][y][x] = max(dp[n][y][x], dp[n - 1][y - b][x] + 1)
                if x >= a:
                    dp[n][y][x] = max(dp[n][y][x], dp[n - 1][y][x - a] + 1)
    print(dp[N][Y][X] if dp[N][Y][X] else -1)
