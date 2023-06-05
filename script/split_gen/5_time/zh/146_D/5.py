def dfs(i, c):
    global color
    color[i] = c
    for j in adj[i]:
        if color[j] == 0:
            dfs(j, c)
n = int(input())
color = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
dfs(1, 1)
print(max(color))
for i in range(1, n):
    print(color[i])
