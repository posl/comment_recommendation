def dfs(v):
    global cnt
    cnt[v] += cnt[v-1]
    for i in range(len(g[v])):
        dfs(g[v][i])
n, q = map(int, input().split())
g = [[] for i in range(n+1)]
cnt = [0 for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
for i in range(q):
    p, x = map(int, input().split())
    cnt[p] += x
dfs(1)
for i in cnt[1:]:
    print(i, end=' ')
print()

if __name__ == '__main__':
    dfs()