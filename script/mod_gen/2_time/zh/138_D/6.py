def dfs(x):
    for i in range(len(g[x])):
        if i == 0:
            continue
        dfs(g[x][i])
        cnt[x] += cnt[g[x][i]]
    return
n, q = map(int, input().split())
g = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
for _ in range(q):
    p, x = map(int, input().split())
    cnt[p] += x
dfs(1)
print(*cnt[1:])

if __name__ == '__main__':
    dfs()