def main():
    n, m = map(int, input().split())
    road = []
    for i in range(m):
        road.append(list(map(int, input().split())))
    road.sort()
    city = [[] for i in range(n)]
    for i in range(m):
        city[road[i][0]-1].append(road[i][1])
    for i in range(n):
        print(len(city[i]))
        for j in range(len(city[i])):
            print(city[i][j])

if __name__ == '__main__':
    main()