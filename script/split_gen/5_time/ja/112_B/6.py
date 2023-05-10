def solve():
    # 入力
    N, T = map(int, input().split())
    routes = []
    for _ in range(N):
        c, t = map(int, input().split())
        routes.append((c, t))
    # 時間 T 以内に帰宅できる経路のうち、コストが最小となる経路のコストを求める
    min_cost = float('inf')
    for c, t in routes:
        if t <= T:
            min_cost = min(min_cost, c)
    # 出力
    if min_cost == float('inf'):
        print('TLE')
    else:
        print(min_cost)
