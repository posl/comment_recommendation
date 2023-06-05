def solve():
    N,M,T = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    # print(N,M,T)
    # print(AB)
    # print(AB[0][0])
    # 电池容量
    battery = N
    # print(battery)
    # 电池电量
    battery = N
    # print(battery)
    # 咖啡馆的停留时间
    # AB = [[9, 11], [13, 17]]
    # print(AB)
    # print(AB[0][0])
    # print(AB[0][1])
    # print(AB[1][0])
    # print(AB[1][1])
    # 电池电量的变化
    # 电池电量变化的时间点
    time = [0]
    for i in range(M):
        time.append(AB[i][0])
        time.append(AB[i][1])
    time.append(T)
    # print(time)
    # 电池电量变化的电量
    battery_list = [N]
    for i in range(1,len(time)):
        if i % 2 == 0:
            battery_list.append(battery_list[i-1] - (time[i] - time[i-1]))
        else:
            battery_list.append(battery_list[i-1] + (time[i] - time[i-1]))
    # print(battery_list)
    # 电池电量变化的判断
    for i in range(len(battery_list)):
        if battery_list[i] <= 0:
            print('No')
            exit()
    print('Yes')
