def main():
    N, M = map(int, input().split())
    # 0-indexed
    adj = [[0] * N for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u][v] = 1
        adj[v][u] = 1
    ans = 0
    for a in range(N):
        for b in range(a+1, N):
            if adj[a][b] == 0:
                continue
            for c in range(b+1, N):
                if adj[b][c] == 0 or adj[c][a] == 0:
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()