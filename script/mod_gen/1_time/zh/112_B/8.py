def func():
    N, T = map(int, input().split())
    cost_time = []
    for i in range(N):
        cost, time = map(int, input().split())
        if time <= T:
            cost_time.append([cost, time])
    if len(cost_time) == 0:
        print("TLE")
    else:
        cost_time.sort(key=lambda x: x[0])
        print(cost_time[0][0])

if __name__ == '__main__':
    func()