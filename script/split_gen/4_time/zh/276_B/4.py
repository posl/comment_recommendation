def main():
    n,m = map(int, input().split())
    road = []
    for i in range(m):
        road.append(list(map(int, input().split())))
    city = [[] for i in range(n)]
    for i in range(m):
        city[road[i][0]-1].append(road[i][1])
        city[road[i][1]-1].append(road[i][0])
    for i in range(n):
        print(len(city[i]), end = ' ')
        for j in range(len(city[i])):
            print(city[i][j], end = ' ')
        print()
