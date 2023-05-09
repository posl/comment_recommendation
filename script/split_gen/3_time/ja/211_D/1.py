def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    dist = [-1] * N
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    if dist[-1] == -1:
        print(0)
    else:
        print(dist.count(dist[-1]))
