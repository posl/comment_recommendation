def countTriangle(graph):
    count = 0
    for i in range(1, len(graph) + 1):
        for j in range(i + 1, len(graph) + 1):
            if graph[i][j] == 1:
                for k in range(j + 1, len(graph) + 1):
                    if graph[i][k] == 1 and graph[j][k] == 1:
                        count += 1
    return count
