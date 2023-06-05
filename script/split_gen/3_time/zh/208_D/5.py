def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    A = [x - 1 for x in A]
    B = [x - 1 for x in B]
    # Floyd-Warshall algorithm
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for i in range(M):
        dist[A[i]][B[i]] = C[i]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    # Count the number of paths
    ans = 0
    for s in range(N):
        for t in range(N):
            for k in range(N):
                if dist[s][t] == dist[s][k] + dist[k][t]:
                    ans += dist[s][t]
                    break
    print(ans)
