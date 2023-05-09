def makeGraph(N, M, edges):
    graph = [[] for i in range(N)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph
