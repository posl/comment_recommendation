def dfs(v, c):
    color[v] = c
    for i in graph[v]:
        if color[i] == -1:
            dfs(i, 1 - c)
N = int(input())
graph = [[] for _ in range(N)]
color = [-1] * N
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w % 2 == 0:
        graph[u].append(v)
        graph[v].append(u)
dfs(0, 0)
for i in range(N):
    print(color[i])

if __name__ == '__main__':
    dfs()