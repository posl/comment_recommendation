def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * N
    Y = [0] * N
    for _ in range(M):
        c, y = map(int, input().split())
        C[c - 1] = c
        Y[c - 1] = y
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i + 1], dp[i] + X[i])
        for j in range(i + 1, N):
            if C[j] == 0:
                break
            dp[j + 1] = max(dp[j + 1], dp[i] + X[i] * (j - i) + Y[j] * (j - i + 1))
    print(dp[N])

if __name__ == '__main__':
    main()