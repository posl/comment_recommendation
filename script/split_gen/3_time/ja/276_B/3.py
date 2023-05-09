def main():
    N, M = map(int, input().split())
    road = [[] for i in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        road[a].append(b)
        road[b].append(a)
    for i in range(1, N+1):
        road[i].sort()
        print(len(road[i]), *road[i])
