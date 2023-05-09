def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # dp[i][j] := i番目までの弁当を選んだとき、たこ焼きがj個以上になる場合の最小個数
    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-A[i]] + 1) ただし、j >= A[i]
    # dp[i][j] = dp[i-1][j] ただし、j < A[i]
    # dp[0][j] = INF ただし、j >= 1
    # dp[0][0] = 0
    dp = [[float('inf')] * (X+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(X+1):
            if j >= A[i-1]:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-A[i-1]] + 1)
            else:
                dp[i][j] = dp[i-1][j]
    # dp[i][j] := i番目までの弁当を選んだとき、たい焼きがj個以上になる場合の最小個数
    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-B[i]] + 1) ただし、j >= B[i]
    # dp[i][j] = dp[i-1][j] ただし、j < B[i]
    # dp[0][j] = INF ただし、j >= 1
    # dp[0][0] = 0
    dp2 = [[float('inf')] * (Y+1) for _ in range(N+1)]
    dp2[0][0] = 0
    for i in range(1, N+1):
        for j in range(Y

if __name__ == '__main__':
    main()