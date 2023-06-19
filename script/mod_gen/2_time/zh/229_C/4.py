def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    max_a = max(A)
    max_b = max(B)
    if max_a > 1000 or max_b > 1000:
        return
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j >= B[i]:
                dp[i + 1][j] = max(dp[i][j - B[i]] + A[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

if __name__ == '__main__':
    main()