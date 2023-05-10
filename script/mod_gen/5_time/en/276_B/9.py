def main():
    n,m = map(int,input().split())
    roads = []
    for i in range(m):
        a,b = map(int,input().split())
        roads.append([a,b])
    cities = []
    for i in range(n):
        cities.append([])
    for i in range(m):
        cities[roads[i][0]-1].append(roads[i][1])
        cities[roads[i][1]-1].append(roads[i][0])
    for i in range(n):
        cities[i].sort()
        print(len(cities[i]))
        print(*cities[i])

if __name__ == '__main__':
    main()