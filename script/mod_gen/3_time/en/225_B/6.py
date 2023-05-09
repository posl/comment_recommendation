def star_graph():
    N = int(input())
    graph = {}
    for i in range(N-1):
        a,b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    for node in graph:
        if len(graph[node]) == N-1:
            print("Yes")
            return
    print("No")
    return
star_graph()

if __name__ == '__main__':
    star_graph()