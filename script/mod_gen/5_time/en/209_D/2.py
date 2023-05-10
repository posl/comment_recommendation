def main():
    n, q = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(n - 1)]
    queries = [list(map(int, input().split())) for _ in range(q)]
    #print(roads)
    #print(queries)
    # make graph
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])
    #print(graph)
    # make parent list
    parents = [0 for _ in range(n + 1)]
    #print(parents)
    # make depth list
    depths = [0 for _ in range(n + 1)]
    #print(depths)
    # make visited list
    visited = [False for _ in range(n + 1)]
    #print(visited)
    # make depth first search
    def dfs(graph, parents, depths, visited, v, p, d):
        #print("v: {}, p: {}, d: {}".format(v, p, d))
        visited[v] = True
        depths[v] = d
        parents[v] = p
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, parents, depths, visited, i, v, d + 1)
    # start depth first search
    dfs(graph, parents, depths, visited, 1, 0, 0)
    #print(parents)
    #print(depths)
    # make lca
    def lca(parents, depths, u, v):
        #print("u: {}, v: {}".format(u, v))
        #print("depths[u]: {}, depths[v]: {}".format(depths[u], depths[v]))
        if depths[u] > depths[v]:
            u, v = v, u
        #print("u: {}, v: {}".format(u, v))
        while depths[u] != depths[v]:
            #print("u: {}, v: {}".format(u, v))
            v = parents[v]
        #print("u: {}, v: {}".format(u, v))
        while u != v:
            #print("u: {}, v: {}".format(u, v))
            u = parents[u]
            v = parents[v]

if __name__ == '__main__':
    main()