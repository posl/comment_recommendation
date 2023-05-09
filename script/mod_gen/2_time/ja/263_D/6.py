def main():
    #入力
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #初期化
    #dp[i][0] : i番目までの要素を操作した後に、左からi番目の要素をLに置き換えた時の最大値
    #dp[i][1] : i番目までの要素を操作した後に、左からi番目の要素をRに置き換えた時の最大値
    #dp[i][2] : i番目までの要素を操作した後に、左からi番目の要素をそのままにする時の最大値
    dp = [[0] * 3 for _ in range(N + 1)]
    dp[0][0] = L
    dp[0][1] = R
    dp[0][2] = 0
    #漸化式
    for i in range(N):
        dp[i + 1][0] = max(dp[i][0] + A[i], dp[i][1] + A[i], dp[i][2] + L)
        dp[i + 1][1] = max(dp[i][0] + R, dp[i][1] + A[i], dp[i][2] + A[i])
        dp[i + 1][2] = max(dp[i][0], dp[i][1], dp[i][2] + A[i])
    #出力
    print(dp[N][0])

if __name__ == '__main__':
    main()