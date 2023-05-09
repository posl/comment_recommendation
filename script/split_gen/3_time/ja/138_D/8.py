def dfs(v, p, c):
    global ans
    ans[v] += c
    for next_v in graph[v]:
        if next_v == p:
            continue
        dfs(next_v, v, ans[v])
n, q = map(int, input().split())
graph = [[] for _ in range(n)]
ans = [0 for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
for _ in range(q):
    p, x = map(int, input().split())
    ans[p-1] += x
dfs(0, -1, 0)
print(*ans)
