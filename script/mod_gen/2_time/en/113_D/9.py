def main():
    h, w, k = map(int, input().split())
    # dp[i][j]: i段目のj番目の経路の数
    dp = [[0 for _ in range(w)] for _ in range(h+1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            # 左に移動
            if j > 0:
                dp[i+1][j-1] += dp[i][j]
            # 右に移動
            if j < w-1:
                dp[i+1][j+1] += dp[i][j]
            # そのまま
            if j >= 0 and j < w:
                dp[i+1][j] += dp[i][j]
    print(dp[h][k-1]%(10**9+7))

if __name__ == '__main__':
    main()