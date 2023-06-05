def dfs(v, p, c):
    color[c] = True
    ans[v] = c
    for u in G[v]:
        if u == p:
            continue
        c += 1
        if c == ans[p]:
            c += 1
        dfs(u, v, c)
        c += 1
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = [0] * N
color = [False] * N
dfs(0, -1, 1)
print(max(ans))
for i in range(N-1):
    print(ans[i])

if __name__ == '__main__':
    dfs()