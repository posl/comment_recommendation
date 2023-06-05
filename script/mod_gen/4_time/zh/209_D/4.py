def main():
    # 读取输入
    N, Q = map(int, input().split())
    # 读取道路信息
    road = []
    for i in range(N - 1):
        road.append(list(map(int, input().split())))
    # 读取查询信息
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # 处理道路信息
    road_dict = {}
    for i in range(N - 1):
        if road[i][0] not in road_dict.keys():
            road_dict[road[i][0]] = [road[i][1]]
        else:
            road_dict[road[i][0]].append(road[i][1])
        if road[i][1] not in road_dict.keys():
            road_dict[road[i][1]] = [road[i][0]]
        else:
            road_dict[road[i][1]].append(road[i][0])
    # 处理查询信息
    for i in range(Q):
        # 从c_i出发能到达的所有城镇
        c_i = query[i][0]
        d_i = query[i][1]
        c_i_towns = [c_i]
        while True:
            new_towns = []
            for j in range(len(c_i_towns)):
                for k in range(len(road_dict[c_i_towns[j]])):
                    if road_dict[c_i_towns[j]][k] not in c_i_towns:
                        new_towns.append(road_dict[c_i_towns[j]][k])
            if len(new_towns) == 0:
                break
            else:
                for j in range(len(new_towns)):
                    c_i_towns.append(new_towns[j])
        # print(c_i_towns)
        if d_i in c_i_towns:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()