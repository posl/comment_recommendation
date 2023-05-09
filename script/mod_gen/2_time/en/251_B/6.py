def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    dp = [[[0] * (W + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][i][0] = 1
    for i in range(N):
        for j in range(i + 1, N + 1):
            for k in range(1, W + 1):
                if k - A[j] >= 0:
                    dp[i][j][k] = dp[i][j - 1][k] + dp[i][j - 1][k - A[j]]
                else:
                    dp[i][j][k] = dp[i][j - 1][k]
    ans = 0
    for i in range(N + 1):
        for j in range(i, N + 1):
            ans += dp[i][j][W]
    print(ans)

if __name__ == '__main__':
    main()