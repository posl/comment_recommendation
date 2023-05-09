def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[float("inf")] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + Y + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - A[i]] + 1)
            if j - B[i] >= 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - B[i]] + 1)
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    if dp[N][X] == float("inf") or dp[N][Y] == float("inf"):
        print(-1)
    else:
        print(min(dp[N][X], dp[N][Y]))

if __name__ == '__main__':
    main()