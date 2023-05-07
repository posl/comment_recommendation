def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[0] = 0
    for i in range(N):
        dp[i + 1] = dp[i] + X[i]
        for j in range(M):
            if i + 1 - C[j] >= 0:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - C[j]] + X[i] + Y[j])
    print(dp[N])

if __name__ == '__main__':
    main()