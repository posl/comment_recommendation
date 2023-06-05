def main():
    #读入数据
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    #dp[i][j]表示从i,j开始游戏时，先手的人能得到的最大分数
    dp = [[0] * w for _ in range(h)]
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if i == h - 1 and j == w - 1:
                continue
            if (i + j) % 2 == 0:
                #先手
                if i == h - 1:
                    dp[i][j] = dp[i][j+1] + (1 if a[i][j+1] == '+' else -1)
                elif j == w - 1:
                    dp[i][j] = dp[i+1][j] + (1 if a[i+1][j] == '+' else -1)
                else:
                    dp[i][j] = max(dp[i][j+1] + (1 if a[i][j+1] == '+' else -1), dp[i+1][j] + (1 if a[i+1][j] == '+' else -1))
            else:
                #后手
                if i == h - 1:
                    dp[i][j] = dp[i][j+1] - (1 if a[i][j+1] == '+' else -1)
                elif j == w - 1:
                    dp[i][j] = dp[i+1][j] - (1 if a[i+1][j] == '+' else -1)
                else:
                    dp[i][j] = min(dp[i][j+1] - (1 if a[i][j+1] == '+' else -1), dp[i+1][j] - (1 if a[i+1][j] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()