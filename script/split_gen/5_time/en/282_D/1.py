def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    visited = [-1] * N
    def dfs(v, c):
        visited[v] = c
        for nv in graph[v]:
            if visited[nv] == c:
                return False
            if visited[nv] == -1 and not dfs(nv, 1-c):
                return False
        return True
    ans = 0
    for i in range(N):
        if visited[i] == -1:
            if dfs(i, 0):
                n0 = visited.count(0)
                n1 = visited.count(1)
                ans += n0 * n1
            else:
                ans = -1
                break
    print(ans)
