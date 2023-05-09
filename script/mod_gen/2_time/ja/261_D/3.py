def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + X[i - 1]
        for j in range(M):
            if C[j] <= i:
                dp[i] = max(dp[i], dp[i - C[j]] + Y[j])
    print(dp[N])

if __name__ == '__main__':
    main()