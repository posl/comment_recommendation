def solve():
    N = int(input())
    x = [0] * N
    y = [0] * N
    p = [0] * N
    for i in range(N):
        x[i], y[i], p[i] = map(int, input().split())
    # print(N, x, y, p)
    # dp[i][j] 表示高桥从第i个蹦床跳到第j个蹦床的最小训练次数
    dp = [[0] * N for _ in range(N)]
    # 初始化dp
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if p[i] * 0 >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                dp[i][j] = 1
            else:
                dp[i][j] = float('inf')
    # print(dp)
    # 动态规划
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j or i == k or j == k:
                    continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    # print(dp)
    # 找出最大值
    ans = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] != float('inf'):
                ans = max(ans, dp[i][j])
    print(ans)

if __name__ == '__main__':
    solve()