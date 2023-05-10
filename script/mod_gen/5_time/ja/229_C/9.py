def main():
    # データ入力
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # DP テーブル定義
    dp = [[0]*(W+1) for i in range(N+1)]
    # DP ループ
    for i in range(N):
        for w in range(W+1):
            if w >= A[i]:
                dp[i+1][w] = max(dp[i][w-A[i]] + B[i], dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]
    # 最適値の出力
    print(dp[N][W])

if __name__ == '__main__':
    main()