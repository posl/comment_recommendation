def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    cities = {i: [] for i in range(1, N + 1)}
    for road in roads:
        cities[road[0]].append(road[1])
        cities[road[1]].append(road[0])
    for i in range(1, N + 1):
        print(len(cities[i]), *sorted(cities[i]))

if __name__ == '__main__':
    main()