def main():
    n,m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    cities = []
    for i in range(n):
        cities.append([])
    for road in roads:
        cities[road[0]-1].append(road[1])
        cities[road[1]-1].append(road[0])
    for city in cities:
        city.sort()
    for city in cities:
        print(len(city), end=" ")
        for c in city:
            print(c, end=" ")
        print()

if __name__ == '__main__':
    main()