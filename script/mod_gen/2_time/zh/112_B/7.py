def main():
    n, t = map(int, input().split())
    cost = []
    time = []
    for i in range(n):
        c, ti = map(int, input().split())
        cost.append(c)
        time.append(ti)
    min_cost = 1001
    for i in range(n):
        if time[i] <= t and cost[i] < min_cost:
            min_cost = cost[i]
    if min_cost == 1001:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    main()