def main():
    M = int(input())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    p = list(map(int, input().split()))
    graph = [[] for _ in range(10)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    for i in range(1, 10):
        graph[i].append(i)
    for i in range(8):
        graph[p[i]].remove(p[i])
    for i in range(8):
        graph[p[i]].append(0)
    graph[0].remove(0)
    for i in range(1, 10):
        graph[i].sort()
    for i in range(1, 10):
        graph[i] = tuple(graph[i])
    graph = tuple(graph)
    visited = set()
    q = [(graph, 0)]
    while q:
        graph, cnt = q.pop()
        if graph in visited:
            continue
        visited.add(graph)
        if graph[1] == (2, 3, 9) and graph[2] == (1, 3, 5) and graph[3] == (1, 2, 6) and graph[4] == (5, 7, 9) and graph[5] == (2, 4, 6, 8) and graph[6] == (3, 5, 9) and graph[7] == (4, 8) and graph[8] == (5, 7) and graph[9] == (1, 4, 6):
            print(cnt)
            return
        for i in range(1, 10):
            for j in range(len(graph[i])):
                for k in range(len(graph[0])):
                    new_graph = list(graph)
                    new_graph[i] = list(new_graph[i])
                    new_graph[0] = list(new_graph[0])
                    new_graph[i].append(new_graph[0][k])
                    new_graph[0].append(new_graph[i][j])
                    new_graph[i].remove(new_graph[0][k])
                    new_graph[0].remove(new_graph[i][j])
                    new_graph[i].sort()
                    new_graph[0].sort
