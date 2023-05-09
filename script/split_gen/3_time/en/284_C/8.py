def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(int, input().split())))
    #print(edges)
    # make graph
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for edge in edges:
        graph[edge[0]-1][edge[1]-1] = 1
        graph[edge[1]-1][edge[0]-1] = 1
    #print(graph)
    # count connected components
    count = 0
    visited = [False for _ in range(N)]
    for i in range(N):
        if visited[i]:
            continue
        count += 1
        queue = [i]
        while queue:
            v = queue.pop(0)
            visited[v] = True
            for j in range(N):
                if graph[v][j] == 1 and not visited[j]:
                    queue.append(j)
    print(count)
