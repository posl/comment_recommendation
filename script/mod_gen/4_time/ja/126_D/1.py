def dfs(v, c):
    color[v] = c
    for next_v, w in graph[v]:
        if color[next_v] != -1:
            continue
        if w % 2 == 0:
            dfs(next_v, c)
        else:
            dfs(next_v, 1 - c)
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))
color = [-1] * n
dfs(0, 0)
for c in color:
    print(c)

if __name__ == '__main__':
    dfs()