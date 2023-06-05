def main():
    # 读入数据
    n, m = map(int, input().split())
    # 城市编号从0开始
    roads = [[int(i)-1 for i in input().split()] for _ in range(m)]
    # 初始化城市
    cities = [[] for _ in range(n)]
    # 为每个城市添加相连的城市
    for road in roads:
        # 两个方向都要添加
        cities[road[0]].append(road[1])
        cities[road[1]].append(road[0])
    # 打印输出
    for city in cities:
        print(len(city), *sorted(city))

if __name__ == '__main__':
    main()