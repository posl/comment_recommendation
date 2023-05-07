def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[float("inf")] * (X + 1) for _ in range(Y + 1)]
    dp[0][0] = 0
    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if x - A[i] >= 0 and y - B[i] >= 0:
                    dp[y][x] = min(dp[y][x], dp[y - B[i]][x - A[i]] + 1)
                dp[y][x] = min(dp[y][x], dp[y][x - A[i]] + 1, dp[y - B[i]][x] + 1)
    if dp[Y][X] == float("inf"):
        print(-1)
    else:
        print(dp[Y][X])
