def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    G = [[] for _ in range(N+1)]
    for i in range(M):
        G[A[i]].append(B[i])
    for i in range(N+1):
        G[i].sort()
    #print(G)
    used = [False] * (N+1)
    ans = []
    def dfs(v):
        used[v] = True
        for nv in G[v]:
            if used[nv]:
                print(-1)
                exit()
            dfs(nv)
        ans.append(v)
    for i in range(1, N+1):
        if not used[i]:
            dfs(i)
    print(*ans[::-1])
