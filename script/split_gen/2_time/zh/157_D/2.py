def DFS(G, v):
    visited[v] = True
    for i in range(len(G[v])):
        if not visited[G[v][i]]:
            DFS(G, G[v][i])
N, M, K = map(int, input().split())
A = []
B = []
C = []
D = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for i in range(K):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)
G = [[] for i in range(N + 1)]
for i in range(M):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])
visited = [False for i in range(N + 1)]
for i in range(K):
    visited[C[i]] = True
    visited[D[i]] = True
for i in range(1, N + 1):
    if not visited[i]:
        DFS(G, i)
        break
ans = [0 for i in range(N + 1)]
for i in range(1, N + 1):
    ans[i] = len(G[i]) - 1 - sum(visited[j] for j in G[i])
print(*ans[1:])
