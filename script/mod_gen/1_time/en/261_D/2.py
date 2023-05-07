def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        dp = [0] * (N + 1)
        for j in range(i + 1):
            dp[j + 1] = max(dp[j + 1], dp[j] + X[j])
            for k in range(M):
                if j + C[k] <= N:
                    dp[j + C[k]] = max(dp[j + C[k]], dp[j] + Y[k])
        ans = max(ans, dp[N])
    print(ans)

if __name__ == '__main__':
    main()