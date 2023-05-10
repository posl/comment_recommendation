def dijkstra(s, N, G):
    color = [0] * N
    d = [float('inf')] * N
    d[s] = 0
    color[s] = 1
    while(1):
        minv = float('inf')
        for i in range(N):
            if color[i] != 2 and d[i] < minv:
                minv = d[i]
                u = i
        if minv == float('inf'):
            break
        color[u] = 2
        for v in range(N):
            if color[v] != 2 and G[u][v] != float('inf'):
                if d[u] + G[u][v] < d[v]:
                    d[v] = d[u] + G[u][v]
                    color[v] = 1
    return d
N,M = map(int,input().split())
G = [[float('inf') for i in range(N)] for j in range(N)]
for i in range(M):
    A,B,C = map(int,input().split())
    G[A-1][B-1] = C
ans = 0
for i in range(N):
    d = dijkstra(i,N,G)
    for j in range(N):
        for k in range(N):
            if d[j] + G[j][k] == d[k]:
                ans += d[j]
print(ans)

if __name__ == '__main__':
    dijkstra()