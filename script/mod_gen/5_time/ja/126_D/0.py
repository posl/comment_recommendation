def dfs(v, c):
    color[v] = c
    for next_v, w in graph[v]:
        if color[next_v] != -1:
            continue
        if w % 2 == 0:
            dfs(next_v, c)
        else:
            dfs(next_v, 1 - c)
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))
color = [-1] * N
dfs(0, 0)
for c in color:
    print(c)

if __name__ == '__main__':
    dfs()