def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    color = [None] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in graph[v]:
            if color[nv] is None:
                color[nv] = color[v] ^ (w % 2)
                stack.append(nv)
    for c in color:
        print(c)
