def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print('N =', N)
    # print('W =', W)
    # print('A =', A)
    # print('B =', B)
    # print('N =', N)
    # print('W =', W)
    # print('A =', A)
    # print('B =', B)
    # dp[i][w] := 使用前i种奶酪，总重量为w时的美味度
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(N):
        for w in range(W + 1):
            if w - B[i] >= 0:
                dp[i + 1][w] = max(dp[i][w], dp[i][w - B[i]] + A[i])
            else:
                dp[i + 1][w] = dp[i][w]
    print(dp[N][W])

if __name__ == '__main__':
    main()