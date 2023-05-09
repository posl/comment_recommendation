def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    connected_cities = [[] for _ in range(N)]
    for road in roads:
        connected_cities[road[0] - 1].append(road[1])
        connected_cities[road[1] - 1].append(road[0])
    for i in range(N):
        connected_cities[i].sort()
        print(len(connected_cities[i]), *connected_cities[i])
    return
