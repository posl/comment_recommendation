def dfs(v, p, c):
    color = 1
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        if color == c:
            color += 1
        ans[G[v][i]] = color
        dfs(G[v][i], v, color)
        color += 1
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
ans = [0] * N
dfs(0, -1, 0)
print(max(ans))
for i in range(N-1):
    print(ans[i+1])
