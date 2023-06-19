def dfs(x, p):
    global ans
    ans.append(x)
    for y in G[x]:
        if y != p:
            dfs(y, x)
            ans.append(x)
    return
N, X, Y = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
ans = []
dfs(X, -1)
ans.append(X)
ans.reverse()
dfs(Y, -1)
print(*ans)

if __name__ == '__main__':
    dfs()