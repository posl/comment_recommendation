def main():
    N = int(input())
    # 1-indexed
    edge = [[] for i in range(N + 1)]
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        edge[u].append([v, w])
        edge[v].append([u, w])
    # 1-indexed
    color = [None for i in range(N + 1)]
    color[1] = 0
    stack = [1]
    while len(stack) > 0:
        u = stack.pop()
        for v, w in edge[u]:
            if color[v] is None:
                color[v] = (color[u] + w) % 2
                stack.append(v)
    for i in range(1, N + 1):
        print(color[i])
