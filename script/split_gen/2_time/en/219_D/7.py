def main():
    #input
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #calc
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j - B[i] >= 0 and k - A[i] >= 0:
                    dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j - B[i]][k - A[i]] + 1)
                elif j - B[i] >= 0:
                    dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j - B[i]][k] + 1)
                elif k - A[i] >= 0:
                    dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k - A[i]] + 1)
    #output
    if dp[N][Y][X] == float('inf'):
        print(-1)
    else:
        print(dp[N][Y][X])
