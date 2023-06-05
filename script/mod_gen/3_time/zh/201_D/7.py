def main():
    # 读入
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    # 从下往上、从右往左依次计算
    dp = [[0] * w for _ in range(h)]
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            # 如果是最后一个，就是自己的得分
            if i == h - 1 and j == w - 1:
                continue
            # 如果是红色，就是对方的得分
            if (i + j) % 2 == 1:
                dp[i][j] = 10 ** 10
                if i + 1 < h:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + (1 if a[i + 1][j] == '-' else -1))
                if j + 1 < w:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + (1 if a[i][j + 1] == '-' else -1))
            # 如果是蓝色，就是自己的得分
            else:
                dp[i][j] = -10 ** 10
                if i + 1 < h:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] - (1 if a[i + 1][j] == '-' else -1))
                if j + 1 < w:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] - (1 if a[i][j + 1] == '-' else -1))
    # 判断结果
    if dp[0][0] == 0:
        print("Draw")
    elif dp[0][0] > 0:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()