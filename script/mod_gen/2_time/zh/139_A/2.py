def dfs(v, p):
    global ans
    ans[v] += ans[p]
    for u in edge[v]:
        if u == p:
            continue
        dfs(u, v)
n, q = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
ans = [0] * (n + 1)
for _ in range(q):
    p, x = map(int, input().split())
    ans[p] += x
dfs(1, 0)
print(*ans[1:])

if __name__ == '__main__':
    dfs()