def main():
    # read input
    N, X, Y = map(int, input().split())
    # N: the number of jewels
    # X: the number of blue jewels of level n converted from a red jewel of level n
    # Y: the number of blue jewels of level n-1 converted from a blue jewel of level n
    # 1. create a graph
    graph = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if j <= i+1:
                graph[i][j] = 1
                graph[j][i] = 1
            elif j == i+2:
                graph[i][j] = X
                graph[j][i] = X
            elif j == i+3:
                graph[i][j] = Y
                graph[j][i] = Y
            else:
                graph[i][j] = 0
                graph[j][i] = 0
    # 2. calculate the shortest path from 0 to N-1
    #    using Dijkstra's algorithm
    dist = [float('inf') for i in range(N)]
    dist[0] = 0
    visited = [False for i in range(N)]
    while True:
        # 2-1. find the node with the minimum distance
        min_dist = float('inf')
        min_dist_node = -1
        for i in range(N):
            if visited[i] == False and dist[i] < min_dist:
                min_dist = dist[i]
                min_dist_node = i
        if min_dist_node == -1:
            break
        visited[min_dist_node] = True
        # 2-2. update the distance of the neighbor nodes
        for i in range(N):
            if graph[min_dist_node][i] > 0:
                dist[i] = min(dist[i], dist[min_dist_node] + graph[min_dist_node][i])
    # 3. output the result
    print(dist[N-1])
