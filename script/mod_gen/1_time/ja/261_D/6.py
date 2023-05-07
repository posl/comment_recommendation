def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C_Y = [list(map(int, input().split())) for _ in range(M)]
    C_Y.sort(key=lambda x: x[0])
    C, Y = zip(*C_Y)
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(M):
            if i + 1 < C[j]:
                break
            dp[i + 1] = max(dp[i + 1], dp[i + 1 - C[j]] + Y[j])
    print(dp[N])

if __name__ == '__main__':
    main()