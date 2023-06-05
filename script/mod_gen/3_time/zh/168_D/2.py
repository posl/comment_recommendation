def dfs(v):
    global ans
    if visited[v]: return
    visited[v] = True
    for u in G[v]:
        if visited[u]: continue
        dfs(u)
    ans.append(v)
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1; B -= 1
    G[A].append(B)
    G[B].append(A)
visited = [False] * N
ans = []
dfs(0)
ans = ans[::-1]
ans = [i + 1 for i in ans]
print("Yes")
print(*ans, sep="\n")

if __name__ == '__main__':
    dfs()