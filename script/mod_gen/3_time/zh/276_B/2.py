def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().split())))
    # print(roads)
    # print(n, m)
    # n, m = 5, 10
    # roads = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [
    #     2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
    # roads = [[3, 6], [1, 3], [5, 6], [2, 5], [1, 2], [1, 6]]
    # print(roads)
    # print(n, m)
    # print(roads)
    cities = [[] for _ in range(n)]
    for road in roads:
        cities[road[0]-1].append(road[1])
        cities[road[1]-1].append(road[0])
    for city in cities:
        city.sort()
    for city in cities:
        print(len(city), end=' ')
        for c in city:
            print(c, end=' ')
        print()

if __name__ == '__main__':
    main()