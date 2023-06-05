def solve():
    # 读取输入
    N, T = map(int, input().split())
    routes = []
    for i in range(N):
        c, t = map(int, input().split())
        routes.append((c, t))
    # 计算最小花费
    min_cost = float('inf')
    for c, t in routes:
        if t <= T:
            min_cost = min(c, min_cost)
    # 输出结果
    if min_cost == float('inf'):
        print('TLE')
    else:
        print(min_cost)

if __name__ == '__main__':
    solve()