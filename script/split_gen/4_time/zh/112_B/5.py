def main():
    # 读取输入
    n, t = map(int, input().split())
    ct = []
    for i in range(n):
        c, t = map(int, input().split())
        ct.append((c, t))
    # 按照时间排序
    ct.sort(key=lambda x: x[1])
    # print(ct)
    # dp[i][j]表示用前i个路线，花费时间为j的最小成本
    dp = [[float('inf')] * (t + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(t + 1):
            if j < ct[i][1]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - ct[i][1]] + ct[i][0])
    # print(dp)
    if dp[n][t] == float('inf'):
        print('TLE')
    else:
        print(dp[n][t])
