def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    visited = [False] * N
    def dfs(v):
        visited[v] = True
        for nv in G[v]:
            if not visited[nv]:
                dfs(nv)
    count = 0
    for v in range(N):
        if not visited[v]:
            dfs(v)
            count += 1
    print(count)
