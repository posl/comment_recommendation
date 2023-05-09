def find_shortest_path(N, M, A, B):
    # initialize graph
    graph = [[] for _ in range(N)]
    for a, b in zip(A, B):
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # initialize distance
    distance = [-1] * N
    distance[0] = 0
    # initialize queue
    queue = [0]
    # initialize path
    path = [0] * N
    path[0] = 1
    while queue:
        current = queue.pop(0)
        for next in graph[current]:
            if distance[next] == -1:
                distance[next] = distance[current] + 1
                queue.append(next)
                path[next] = path[current]
            elif distance[next] == distance[current] + 1:
                path[next] += path[current]
                path[next] %= 1000000007
    return path[N-1]

if __name__ == '__main__':
    find_shortest_path()