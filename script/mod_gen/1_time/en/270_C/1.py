def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    queue = [X]
    while queue:
        v = queue.pop(0)
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                queue.append(nv)
    for i in range(N):
        if dist[i] == -1:
            continue
        for j in range(i+1, N):
            if dist[j] == -1:
                continue
            if dist[i] + dist[j] + 1 == dist[Y]:
                print(i+1, j+1)
main()
