Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    n, t = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(n)]
    # print(ct)
    # 用于保存结果
    result = 1001
    # 遍历所有的路线
    for c, t_ in ct:
        # 如果时间不超过限制
        if t_ <= t:
            # 更新结果
            result = min(result, c)
    # 如果结果没有更新
    if result == 1001:
        # 打印TLE
        print('TLE')
    # 否则
    else:
        # 打印结果
        print(result)

=======
Suggestion 2

def findMinCost(N, T, cost, time):
    minCost = 1000 * 1000
    for i in range(N):
        if time[i] <= T and cost[i] < minCost:
            minCost = cost[i]
    return minCost

=======
Suggestion 3

def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        c.append(list(map(int, input().split())))
    c.sort(key=lambda x: x[1])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            exit()
    print("TLE")

=======
Suggestion 4

def input():
    N, T = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(N)]
    return N, T, ct

=======
Suggestion 5

def main():
    n,t = map(int,input().split())
    c = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    c.sort(key = lambda x:x[1])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            return
    print('TLE')

=======
Suggestion 6

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

=======
Suggestion 7

def problems112_b():
    n, t = map(int, input().split())
    c = []
    for _ in range(n):
        c.append(list(map(int, input().split())))
    c.sort(key=lambda x: x[1])
    for i in range(n):
        if c[i][1] <= t:
            print(c[i][0])
            break
    else:
        print("TLE")

=======
Suggestion 8

def main():
    n,t = map(int,input().split())
    c = []
    tt = []
    for i in range(n):
        a,b = map(int,input().split())
        c.append(a)
        tt.append(b)
    min_cost = 1001
    for i in range(n):
        if tt[i] <= t and c[i] < min_cost:
            min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

=======
Suggestion 9

def get_input():
    input_list = []
    while True:
        try:
            input_list.append(list(map(int, input().split())))
        except EOFError:
            break
    return input_list

=======
Suggestion 10

def main():
    n, t = map(int, input().split())
    c = []
    time = []
    for i in range(n):
        c1, time1 = map(int, input().split())
        c.append(c1)
        time.append(time1)
    min_cost = 1001
    for i in range(n):
        if time[i] <= t:
            if min_cost > c[i]:
                min_cost = c[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)
