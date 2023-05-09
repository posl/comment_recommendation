def dfs(v, p, c):
    global ans
    ans[v-1] += c
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        dfs(G[v][i], v, c)
N, Q = map(int, input().split())
G = [[] for i in range(N+1)]
ans = [0] * N
for i in range(N-1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in range(Q):
    p,x = map(int, input().split())
    dfs(p, -1, x)
print(*ans)

if __name__ == '__main__':
    dfs()