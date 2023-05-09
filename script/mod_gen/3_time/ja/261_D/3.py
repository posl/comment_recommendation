def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    dp = [0] * (N+1)
    bonus = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = dp[i-1] + X[i-1]
        bonus[i] = bonus[i-1]
        for j in range(M):
            if i >= C[j]:
                bonus[i] = max(bonus[i], bonus[i-C[j]] + Y[j])
        dp[i] = max(dp[i], dp[i-1], dp[i] + bonus[i])
    print(dp[N])

if __name__ == '__main__':
    main()