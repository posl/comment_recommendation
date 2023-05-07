def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N)]
    for a, b in ab:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    visited = [-1] * N
    for i in range(N):
        if visited[i] != -1:
            continue
        stack = [i]
        visited[i] = 0
        while stack:
            v = stack.pop()
            for w in graph[v]:
                if visited[w] == -1:
                    visited[w] = visited[v] ^ 1
                    stack.append(w)
                elif visited[w] == visited[v]:
                    print('No')
                    exit()
    print('Yes')
