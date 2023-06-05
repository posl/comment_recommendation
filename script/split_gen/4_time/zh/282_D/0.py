def main():
    n,m = map(int, input().split())
    #print(n,m)
    #print(type(n),type(m))
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    #print(edges)
    #print(type(edges))
    graph = {}
    for i in range(1,n+1):
        graph[i] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    #print(graph)
    #print(type(graph))
    ans = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if j not in graph[i]:
                #print(i,j)
                #print(graph[i])
                #print(graph[j])
                ans += 1
    print(ans)
