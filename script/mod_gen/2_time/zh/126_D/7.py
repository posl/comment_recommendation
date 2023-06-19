def dfs(u, c, d):
    color[u] = c
    for v, w in adj[u]:
        if color[v] != -1:
            continue
        dfs(v, c ^ (w & 1), d + w)
n = int(input())
adj = [[] for _ in range(n)]
color = [-1] * n
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))
dfs(0, 0, 0)
for i in range(n):
    print(color[i])

if __name__ == '__main__':
    dfs()