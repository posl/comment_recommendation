def main():
    N, M = map(int, input().split())
    roads = []
    for i in range(M):
        roads.append(list(map(int, input().split())))
    cities = [[0] for _ in range(N)]
    for i in range(M):
        cities[roads[i][0]-1].append(roads[i][1])
        cities[roads[i][1]-1].append(roads[i][0])
    for i in range(N):
        cities[i].sort()
    for i in range(N):
        print(len(cities[i])-1, end=" ")
        for j in range(1, len(cities[i])):
            print(cities[i][j], end=" ")
        print()
