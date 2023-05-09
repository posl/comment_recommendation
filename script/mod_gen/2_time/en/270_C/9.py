def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    X -= 1
    Y -= 1
    #print(X, Y)
    edges = []
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
    #print(edges)
    #print(edges)
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for u, v in edges:
        dist[u][v] = 1
        dist[v][u] = 1
    #print(dist)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dist[j][i] != -1 and dist[i][k] != -1:
                    if dist[j][k] == -1 or dist[j][k] > dist[j][i] + dist[i][k]:
                        dist[j][k] = dist[j][i] + dist[i][k]
    #print(dist)
    ans = [0] * N
    for i in range(N):
        for j in range(N):
            if dist[i][j] == -1:
                continue
            ans[dist[i][j]] += 1
    for i in range(1, N):
        print(ans[i]//2)

if __name__ == '__main__':
    main()