def dfs(v, p):
    global ans
    ans.append(v+1)
    for nv in to[v]:
        if nv == p:
            continue
        dfs(nv, v)
        ans.append(v+1)
n, x, y = map(int, input().split())
x -= 1
y -= 1
to = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    to[u].append(v)
    to[v].append(u)
ans = []
dfs(x, -1)
print(*ans)

if __name__ == '__main__':
    dfs()