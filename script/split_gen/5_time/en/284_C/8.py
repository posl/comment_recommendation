def main():
    n,m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    #print(edges)
    graph = [[] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if edges[j][0] == i+1:
                graph[i].append(edges[j][1])
            if edges[j][1] == i+1:
                graph[i].append(edges[j][0])
    #print(graph)
    visited = [False for i in range(n)]
    def dfs(graph, v, visited):
        visited[v] = True
        for i in range(len(graph[v])):
            if not visited[graph[v][i]-1]:
                dfs(graph, graph[v][i]-1, visited)
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)
    print(count)
