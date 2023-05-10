def floydWarshall(graph, V): 
    dist = list(map(lambda i : list(map(lambda j : j , i)) , graph)) 
    for k in range(V): 
        for i in range(V): 
            for j in range(V): 
                dist[i][j] = min(dist[i][j] , dist[i][k]+ dist[k][j]) 
    return dist
N, M = map(int,input().split())
graph = [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int,input().split())
    graph[A-1][B-1] = C
dist = floydWarshall(graph, N)
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if dist[i][k] + dist[k][j] == dist[i][j]:
                ans += dist[i][j]
print(ans)
