def dfs(x, y):
    if x == y:
        return [x]
    for i in range(len(G[x])):
        if not visited[G[x][i]]:
            visited[G[x][i]] = True
            res = dfs(G[x][i], y)
            if res:
                res.insert(0, x)
                return res
    return []
N, X, Y = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
visited = [False] * N
visited[X-1] = True
res = dfs(X-1, Y-1)
print(*[i+1 for i in res])

if __name__ == '__main__':
    dfs()