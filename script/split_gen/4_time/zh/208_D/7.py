def floyd_warshall(n, m, road):
    '''floyd_warshall'''
    inf = float('inf')
    dist = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i in range(m):
        dist[road[i][0]-1][road[i][1]-1] = road[i][2]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist
