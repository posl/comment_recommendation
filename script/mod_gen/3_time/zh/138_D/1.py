def dfs(v, p, x):
    global ans
    ans[v] += x
    for u in g[v]:
        if u != p:
            dfs(u, v, x)
n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
ans = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    dfs(p - 1, -1, x)
print(*ans)

if __name__ == '__main__':
    dfs()