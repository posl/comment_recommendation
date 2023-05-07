def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    # dp[i][j] := マス(i,j)に駅を建設するときの鉄道建設費用の最小値
    dp = [[float('inf') for _ in range(W)] for _ in range(H)]
    ans = float('inf')
    # dp[i][j]の更新
    for i in range(H):
        for j in range(W):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            ans = min(ans, A[i][j] + C*(i+j) + dp[i][j])
            dp[i][j] = min(dp[i][j], A[i][j] - C*(i+j))
    # dp[i][j]の更新
    for i in range(H):
        for j in range(W):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            ans = min(ans, A[i][j] + C*(i+j) + dp[i][j])
            dp[i][j] = min(dp[i][j], A[i][j] - C*(i+j))
    print(ans)

if __name__ == '__main__':
    main()