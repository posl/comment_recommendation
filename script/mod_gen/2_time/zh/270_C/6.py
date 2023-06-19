def dfs(v, p):
    global ans
    ans.append(v)
    for i in G[v]:
        if i != p:
            dfs(i, v)
            ans.append(v)
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
ans.pop()
dfs(Y, -1)
ans.append(Y)
print(*ans)

if __name__ == '__main__':
    dfs()