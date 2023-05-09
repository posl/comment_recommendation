def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    # 0-indexed
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    # 0: not visited, 1: white, 2: black
    color = [0] * N
    def dfs(v, c):
        color[v] = c
        for nv in graph[v]:
            if color[nv] == 0:
                if not dfs(nv, 3-c):
                    return False
            elif color[nv] == c:
                return False
        return True
    ans = 0
    for i in range(N):
        if color[i] == 0:
            if dfs(i, 1):
                ans += color.count(1) * color.count(2)
            else:
                ans = -1
                break
    print(ans)
