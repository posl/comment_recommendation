def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * (N + 1)
    Y = [0] * (N + 1)
    for _ in range(M):
        c, y = map(int, input().split())
        C[c] = c
        Y[c] = y
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + X[i - 1]
        if C[i] > 0:
            dp[i] = max(dp[i], dp[i - C[i]] + X[i - 1] + Y[C[i]])
    print(max(dp))

if __name__ == '__main__':
    main()