def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        adj[A].append(B)
    P = []
    visited = [False] * (N+1)
    def dfs(v):
        visited[v] = True
        for u in adj[v]:
            if visited[u]:
                return False
            if not dfs(u):
                return False
        P.append(v)
        return True
    for v in range(1, N+1):
        if not visited[v] and not dfs(v):
            print(-1)
            return
    print(*P)

if __name__ == '__main__':
    main()