def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    MAX = 10 ** 5 + 1
    dp = [[0] * MAX for _ in range(N + 1)]
    for i in range(N):
        for j in range(MAX):
            if j >= B[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - B[i]] + A[i])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

if __name__ == '__main__':
    main()