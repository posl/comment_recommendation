def main():
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    cities = [set() for _ in range(n)]
    for road in roads:
        cities[road[0]-1].add(road[1])
        cities[road[1]-1].add(road[0])
    for city in cities:
        print(len(city), end=' ')
        print(*sorted(city))

if __name__ == '__main__':
    main()