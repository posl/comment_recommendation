def get_graph():
    n,m = map(int,input().split())
    graph = [[0 for i in range(n)] for i in range(n)]
    for i in range(m):
        u,v = map(int,input().split())
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1
    return graph
