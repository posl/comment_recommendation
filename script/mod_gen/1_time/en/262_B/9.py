def solve():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    # 1-indexed to 0-indexed
    edges = [(a - 1, b - 1) for a, b in edges]
    # create adjacency matrix
    adj = [[False for _ in range(N)] for _ in range(N)]
    for a, b in edges:
        adj[a][b] = True
        adj[b][a] = True
    # count triangles
    ans = 0
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                if adj[a][b] and adj[b][c] and adj[c][a]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    solve()