def dfs(v, p, c):
    color[c] = True
    ans[v] = c
    for u in g[v]:
        if u == p:
            continue
        nc = 1
        while color[nc]:
            nc += 1
        dfs(u, v, nc)
N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
color = [False] * N
ans = [0] * N
dfs(0, -1, 0)
print(max(ans))
for i in range(N-1):
    print(ans[i]+1)

if __name__ == '__main__':
    dfs()