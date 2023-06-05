def dfs(v, p, d):
    depth[v] = d
    for i in range(len(G[v])):
        if G[v][i] != p:
            dfs(G[v][i], v, d+1)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
depth = [0] * N
dfs(0, -1, 0)
ans = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    ans[p] += x
for i in range(N):
    print(ans[i], end=' ')
print()
for i in range(N):
    print(ans[i], end=' ')
print()

if __name__ == '__main__':
    dfs()