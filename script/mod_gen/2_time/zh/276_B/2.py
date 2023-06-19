def main():
    [N, M] = [int(x) for x in input().split()]
    roads = [[int(x) for x in input().split()] for i in range(M)]
    #print(roads)
    cities = [[] for i in range(N)]
    for i in range(M):
        cities[roads[i][0]-1].append(roads[i][1])
        cities[roads[i][1]-1].append(roads[i][0])
    #print(cities)
    #cities = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    for i in range(N):
        cities[i].sort()
        cities[i].insert(0,len(cities[i]))
        print(*cities[i])
    return 0

if __name__ == '__main__':
    main()