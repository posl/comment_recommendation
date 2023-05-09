def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().split())))
    #print(roads)
    cities = {}
    for road in roads:
        if road[0] not in cities:
            cities[road[0]] = [road[1]]
        else:
            cities[road[0]].append(road[1])
        if road[1] not in cities:
            cities[road[1]] = [road[0]]
        else:
            cities[road[1]].append(road[0])
    #print(cities)
    for i in range(1, n+1):
        if i in cities:
            print(len(cities[i])+1, end=" ")
            print(*sorted(cities[i]))
        else:
            print(0)

if __name__ == '__main__':
    main()