def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    # dp[i][j] = (i, j) にたどり着くのに必要な最小コスト
    dp = [[0] * W for _ in range(H)]
    # 初期条件
    dp[0][0] = 1
    # 動的計画法
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if C[i][j] == "#":
                dp[i][j] = 0
            else:
                if i >= 1:
                    dp[i][j] += dp[i - 1][j]
                if j >= 1:
                    dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()