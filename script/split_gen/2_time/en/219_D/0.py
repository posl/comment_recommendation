def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0][0] = 0
    for i in range(1, N + 1):
        for j in range(1, Y + 1):
            for k in range(1, X + 1):
                if j - B[i - 1] < 0 or k - A[i - 1] < 0:
                    dp[i][j][k] = dp[i - 1][j][k]
                else:
                    dp[i][j][k] = min(dp[i - 1][j][k], dp[i - 1][j - B[i - 1]][k - A[i - 1]] + 1)
    if dp[N][Y][X] == float('inf'):
        print(-1)
    else:
        print(dp[N][Y][X])
