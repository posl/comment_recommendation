def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    # dp[i][j]: i段目のj本目の縦線にたどり着く場合の数
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1
    # 横線を引く場所を全探索
    for i in range(H):
        for mask in range(1 << (W-1)):
            # 横線の連続をチェック
            if '11' in bin(mask):
                continue
            # 横線の左右の縦線を決定
            next = [j for j in range(W)]
            for j in range(W-2):
                if (mask >> j) & 1:
                    next[j+1] = next[j]
            for j in range(W-1, 0, -1):
                if (mask >> (j-1)) & 1:
                    next[j-1] = next[j]
            # dpテーブルを更新
            for j in range(W):
                dp[i+1][next[j]] += dp[i][j]
                dp[i+1][next[j]] %= MOD
    print(dp[H][K-1])

if __name__ == '__main__':
    main()