def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for i in range(M)]
    cities = [[] for i in range(N)]
    for i in range(M):
        cities[roads[i][0] - 1].append(roads[i][1])
        cities[roads[i][1] - 1].append(roads[i][0])
    for i in range(N):
        cities[i].sort()
        cities[i].insert(0, len(cities[i]))
        print(' '.join(map(str, cities[i])))
