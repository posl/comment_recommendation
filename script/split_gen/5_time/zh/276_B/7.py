def main():
    n, m = map(int, input().split())
    #print(n, m)
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    #print(roads)
    cities = []
    for i in range(n):
        cities.append([])
    for road in roads:
        cities[road[0] - 1].append(road[1])
        cities[road[1] - 1].append(road[0])
    #print(cities)
    for city in cities:
        city.sort()
    #print(cities)
    for city in cities:
        print(len(city), end=' ')
        for c in city:
            print(c, end=' ')
        print()
