def solve():
    N, T = map(int, input().split())
    costs = []
    times = []
    for _ in range(N):
        c, t = map(int, input().split())
        costs.append(c)
        times.append(t)
    min_cost = 1001
    for i in range(N):
        if times[i] <= T:
            min_cost = min(min_cost, costs[i])
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)
