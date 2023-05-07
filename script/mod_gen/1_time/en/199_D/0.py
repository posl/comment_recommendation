def solve():
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    if M == 0:
        print(3**N)
        return
    G = [[] for _ in range(N)]
    for i in range(M):
        G[A[i]-1].append(B[i]-1)
        G[B[i]-1].append(A[i]-1)
    for i in range(N):
        G[i].sort()
    for i in range(N):
        G[i] = tuple(G[i])
    G = tuple(G)
    if M == (N*(N-1))//2:
        print(0)
        return
    #print(G)
    def dfs(v, c, used):
        if used[c][v]:
            return
        used[c][v] = True
        for u in G[v]:
            dfs(u, c^1, used)
            dfs(u, c^2, used)
    used = [[False]*N for _ in range(3)]
    dfs(0, 0, used)
    dfs(0, 1, used)
    dfs(0, 2, used)
    #print(used)
    ans = 3**N
    for i in range(N):
        if used[0][i] and used[1][i] and used[2][i]:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    solve()