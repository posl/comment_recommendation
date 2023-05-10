def main():
    n,m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    cities = [[] for _ in range(n)]
    for road in roads:
        cities[road[0] - 1].append(road[1])
        cities[road[1] - 1].append(road[0])
    for city in cities:
        print(len(city), *sorted(city))

if __name__ == '__main__':
    main()