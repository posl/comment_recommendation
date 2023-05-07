def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    roads.sort()
    connections = [[] for _ in range(N)]
    for road in roads:
        connections[road[0]-1].append(road[1])
        connections[road[1]-1].append(road[0])
    for i in range(N):
        print(len(connections[i]), end=' ')
        for j in range(len(connections[i])):
            print(connections[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()