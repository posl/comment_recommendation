def solve():
    # 读入行李数，箱子数，查询数
    n, m, q = map(int, input().split())
    # 读入行李的大小和价值
    wv = [list(map(int, input().split())) for _ in range(n)]
    # 读入箱子的大小
    x = list(map(int, input().split()))
    # 读入查询
    query = [list(map(int, input().split())) for _ in range(q)]
    # 箱子的大小降序排列
    x.sort(reverse=True)
    # 箱子的大小，行李的大小，行李的价值
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(m + 1)]
    # 遍历箱子
    for i in range(m):
        # 遍历行李
        for j in range(n):
            # 遍历行李的价值
            for k in range(wv[j][1], m + 1):
                # 更新dp
                dp[i + 1][k][j + 1] = max(dp[i + 1][k][j + 1], dp[i][k - wv[j][1]][j] + wv[j][0])
    # 遍历查询
    for l, r in query:
        # 初始化箱子的大小
        y = x[:l - 1] + x[r:]
        # 箱子的大小降序排列
        y.sort(reverse=True)
        # 初始化答案
        ans = 0
        # 遍历箱子
        for i in range(m):
            # 遍历行李
            for j in range(n):
                # 遍历行李的价值
                for k in range(wv[j][1], m + 1):
                    # 更新答案
                    ans = max(ans, dp[i + 1][k][j + 1])
        # 打印答案
        print(ans)
solve()
