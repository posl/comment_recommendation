def main():
    # read input
    N, Q = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # create graph
    graph = [set() for _ in range(N)]
    for i, (c, *args) in enumerate(queries):
        if c == 1:
            x, y = args
            graph[x - 1].add(y - 1)
            graph[y - 1].add(x - 1)
        elif c == 2:
            x, y = args
            graph[x - 1].remove(y - 1)
            graph[y - 1].remove(x - 1)
        else:
            x = args[0]
            visited = [False] * N
            visited[x - 1] = True
            queue = [x - 1]
            while queue:
                node = queue.pop()
                for child in graph[node]:
                    if not visited[child]:
                        visited[child] = True
                        queue.append(child)
            print(sum(visited), *sorted([i + 1 for i, v in enumerate(visited) if v]))
    return
