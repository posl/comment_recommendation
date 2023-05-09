def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(X + 1):
            if j - A[i - 1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i - 1]] + B[i - 1])
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
    for i in range(N + 1):
        if dp[i][X] >= Y:
            print(i)
            return
    print(-1)
