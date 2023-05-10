def dfs(v, p):
    global flag
    if visit[v]:
        if visit[v] == 1:
            flag = 0
        return
    visit[v] = 1
    for i in G[v]:
        if i == p:
            continue
        dfs(i, v)
    visit[v] = 2
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
visit = [0]*N
flag = 1
dfs(0, -1)

if __name__ == '__main__':
    dfs()