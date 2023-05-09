def make_graph(n, sx, sy, tx, ty, x, y, r):
    graph = []
    for i in range(n):
        graph.append([])
    graph.append([])
    graph.append([])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 <= (r[i] + r[j]) ** 2:
                graph[i].append(j)
                graph[j].append(i)
        if (x[i] - sx) ** 2 + (y[i] - sy) ** 2 <= r[i] ** 2:
            graph[n].append(i)
            graph[i].append(n)
        if (x[i] - tx) ** 2 + (y[i] - ty) ** 2 <= r[i] ** 2:
            graph[n + 1].append(i)
            graph[i].append(n + 1)
    return graph

if __name__ == '__main__':
    make_graph()