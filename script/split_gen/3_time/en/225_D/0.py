def main():
    N, Q = map(int, input().split())
    graph = [[] for i in range(N+1)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if len(query) == 3:
            graph[query[1]].append(query[2])
            graph[query[2]].append(query[1])
        elif len(query) == 2:
            graph[query[1]].remove(query[2])
            graph[query[2]].remove(query[1])
        elif len(query) == 1:
            visited = [False]*(N+1)
            visited[0] = True
            visited[query[0]] = True
            queue = [query[0]]
            print(len(graph[query[0]]), end=" ")
            while len(queue) > 0:
                current = queue.pop(0)
                for next in graph[current]:
                    if not visited[next]:
                        print(next, end=" ")
                        visited[next] = True
                        queue.append(next)
            print()
