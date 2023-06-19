def main():
    # 读取输入
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    # dp[i][j]表示从(i,j)到达(h-1,w-1)的最大分数差
    dp = [[0]*w for _ in range(h)]
    # 从后往前
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            # 如果是最后一个元素
            if i == h-1 and j == w-1:
                continue
            # 如果是最后一行
            if i == h-1:
                if a[i][j] == '+':
                    dp[i][j] = dp[i][j+1]
                else:
                    dp[i][j] = dp[i][j+1] - 1
            # 如果是最后一列
            elif j == w-1:
                if a[i][j] == '+':
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] - 1
            # 如果不是最后一行或最后一列
            else:
                if a[i][j] == '+':
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) - 1
    # 输出结果
    if dp[0][0] == 0:
        print('Draw')
    elif dp[0][0] > 0:
        print('Takahashi')
    else:
        print('Aoki')
