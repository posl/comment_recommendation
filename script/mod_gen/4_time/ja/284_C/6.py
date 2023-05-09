def dfs(x):
    seen[x] = True
    for i in edge[x]:
        if not seen[i]:
            dfs(i)
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
seen = [False] * n
ans = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        ans += 1
print(ans)

if __name__ == '__main__':
    dfs()