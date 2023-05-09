def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = [0] + A
    B = [0] + B
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, X + 1):
            if j == 1:
                dp[i][j] = A[i] + B[i]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + A[i] + B[i], dp[i][j - 1] + B[i])
    print(dp[N][X])

if __name__ == '__main__':
    main()