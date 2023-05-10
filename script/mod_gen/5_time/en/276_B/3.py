def problem276_b():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b = map(int, input().split())
        roads.append([a, b])
    roads.sort()
    cities = [[] for _ in range(n)]
    for road in roads:
        cities[road[0] - 1].append(road[1])
    for city in cities:
        print(len(city), *city)

if __name__ == '__main__':
    problem276_b()