def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[0] * (X + Y + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(X + Y + 1):
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
            if j - A[i] >= 0:
                dp[i + 1][j] = max(dp[i][j - A[i]] + B[i], dp[i + 1][j])
            if j - B[i] >= 0:
                dp[i + 1][j] = max(dp[i][j - B[i]] + A[i], dp[i + 1][j])
    ans = -1
    for i in range(X + Y + 1):
        if X <= dp[N][i] and Y <= i - dp[N][i]:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()