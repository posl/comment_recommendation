def main():
    # 读入数据
    h, w, k = map(int, input().split())
    # 初始化二维列表
    dp = [[0] * w for _ in range(h + 1)]
    # 初始条件
    dp[0][0] = 1
    # 开始迭代
    for i in range(h):
        # 迭代过程中，dp[i][j]表示从第i-1行的第j-1列到第i行的第j-1列的路径数
        for j in range(w):
            # 遍历第i-1行的每个节点
            for p in range(1 << (w - 1)):
                # 遍历每个节点的右边是否有横线
                for q in range(w - 2):
                    # 如果有两个相邻的横线，跳过
                    if (p >> q) & 1 and (p >> (q + 1)) & 1:
                        continue
                # 如果有横线，跳过
                if (p >> j) & 1:
                    continue
                # 如果在第一列有横线，跳过
                if j > 0 and (p >> (j - 1)) & 1:
                    continue
                # 如果在最后一列有横线，跳过
                if j < w - 1 and (p >> j) & 1:
                    continue
                # 没有横线，更新路径数
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= 1000000007
    # 打印结果
    print(dp[h][k - 1])

if __name__ == '__main__':
    main()