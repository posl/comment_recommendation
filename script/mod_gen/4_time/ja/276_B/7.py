def main():
    N, M = map(int, input().split())
    roads = []
    for i in range(M):
        roads.append(list(map(int, input().split())))
    cities = [[] for i in range(N)]
    for road in roads:
        cities[road[0] - 1].append(road[1])
        cities[road[1] - 1].append(road[0])
    for city in cities:
        print(len(city), *city)

if __name__ == '__main__':
    main()