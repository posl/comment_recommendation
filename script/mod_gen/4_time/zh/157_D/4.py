def dfs(v, c):
    color[v] = c
    for i in range(len(graph[v])):
        if color[graph[v][i]] == c:
            return False
        if color[graph[v][i]] == 0 and (not dfs(graph[v][i], -c)):
            return False
    return True
n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
color = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
for i in range(n):
    if color[i] == 0:
        if not dfs(i, 1):
            print(-1)
            exit()
cnt = [0] * n
for i in range(n):
    cnt[i] = len(graph[i])
for i in range(k):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        cnt[c - 1] -= 1
        cnt[d - 1] -= 1
print(*cnt)

if __name__ == '__main__':
    dfs()