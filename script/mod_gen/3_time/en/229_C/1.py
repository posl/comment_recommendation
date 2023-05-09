def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # dp[i][j] = i番目までの品物の中から、重さがj以下となるように選んだときの、価値の総和の最大値
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= A[i]:
                dp[i+1][j] = max(dp[i][j-A[i]] + B[i], dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])
main()

if __name__ == '__main__':
    main()