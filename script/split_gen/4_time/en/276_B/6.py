def main():
    n,m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    roads.sort()
    cities = [[] for _ in range(n)]
    for road in roads:
        cities[road[0]-1].append(road[1])
        cities[road[1]-1].append(road[0])
    for city in cities:
        print(len(city), *city)
