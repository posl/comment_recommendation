def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M)
    # print(roads)
    # 从任意城市出发，能到达的城市
    can_reach = [set() for _ in range(N)]
    for road in roads:
        can_reach[road[0]-1].add(road[1]-1)
    # print(can_reach)
    # 从任意城市出发，能到达的城市
    can_be_reached = [set() for _ in range(N)]
    for road in roads:
        can_be_reached[road[1]-1].add(road[0]-1)
    # print(can_be_reached)
    # 从任意城市出发，能到达的城市
    can_reach_2 = [set() for _ in range(N)]
    for road in roads:
        for city in can_reach[road[0]-1]:
            can_reach_2[road[0]-1].add(city)
            can_reach_2[road[0]-1].update(can_reach[city])
    # print(can_reach_2)
    # 从任意城市出发，能到达的城市
    can_be_reached_2 = [set() for _ in range(N)]
    for road in roads:
        for city in can_be_reached[road[1]-1]:
            can_be_reached_2[road[1]-1].add(city)
            can_be_reached_2[road[1]-1].update(can_be_reached[city])
    # print(can_be_reached_2)
    # 从任意城市出发，能到达的城市
    can_reach_3 = [set() for _ in range(N)]
    for road in roads:
        for city in can_reach_2[road[0]-1]:
            can_reach_3[road[0]-1].add(city)
            can_reach_3[road[0]-1].update(can_reach_2[city])
    # print(can_reach_3)
    # 从任意城市出发，能到达的城市

if __name__ == '__main__':
    main()