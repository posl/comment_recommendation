def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N, X, Y = map(int, input().split())
    X, Y = X-1, Y-1
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        graph[a].append(b)
        graph[b].append(a)
    dist = [-1]*N
    dist[X] = 0
    def dfs(v):
        for u in graph[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                dfs(u)
    dfs(X)
    for i in range(N):
        if i == X:
            continue
        print(dist[i])
