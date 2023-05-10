def solve():
    n, t = map(int, input().split())
    cost_list = []
    time_list = []
    for i in range(n):
        cost, time = map(int, input().split())
        cost_list.append(cost)
        time_list.append(time)
    cost_list = [cost for (time, cost) in sorted(zip(time_list, cost_list))]
    time_list.sort()
    for i in range(n):
        if time_list[i] <= t:
            print(cost_list[i])
            return
    print("TLE")

if __name__ == '__main__':
    solve()