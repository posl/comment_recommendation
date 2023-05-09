def mincost():
    n, t = map(int, input().split())
    cost = [0] * n
    time = [0] * n
    for i in range(n):
        cost[i], time[i] = map(int, input().split())
    min_cost = 1001
    for i in range(n):
        if time[i] <= t:
            if cost[i] < min_cost:
                min_cost = cost[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    mincost()