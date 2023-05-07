def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # dp[i][j] は i 番目まで決めたとき、j 以下の値を持つ数列の個数
    dp = [[0] * 3001 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        # 累積和
        for j in range(1, 3001):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 998244353
        # 範囲を絞る
        for j in range(A[i - 1], B[i - 1] + 1):
            dp[i][j] = dp[i - 1][j]
    print(dp[N][3000])

if __name__ == '__main__':
    main()