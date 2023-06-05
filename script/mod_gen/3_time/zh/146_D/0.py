def dfs(v, p):
    c = 1
    for u in graph[v]:
        if u == p:
            continue
        if c == color[v]:
            c += 1
        color[u] = c
        c += 1
        dfs(u, v)
    k[0] = max(k[0], c - 1)
n = int(input())
graph = [[] for _ in range(n + 1)]
color = [0] * (n + 1)
k = [0]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
color[1] = 1
dfs(1, -1)
print(k[0])
for i in range(1, n):
    print(color[i + 1])

if __name__ == '__main__':
    dfs()