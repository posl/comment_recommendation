def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        G[A].append(B)
        G[B].append(A)
    
    def dfs(v):
        if v == N:
            return 1
        res = 0
        for c in range(3):
            for u in G[v]:
                if C[u] == c:
                    break
            else:
                C[v] = c
                res += dfs(v + 1)
        return res
    
    C = [-1] * N
    print(dfs(0))

if __name__ == '__main__':
    solve()