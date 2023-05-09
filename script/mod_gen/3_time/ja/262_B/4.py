def main():
    N, M = map(int, input().split())
    
    graph = [[0] * N for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = 1
        graph[v][u] = 1
    
    ans = 0
    for a in range(N):
        for b in range(a + 1, N):
            if graph[a][b] == 0:
                continue
            for c in range(b + 1, N):
                if graph[b][c] == 0 or graph[c][a] == 0:
                    continue
                ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()