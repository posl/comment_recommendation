def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edge[u - 1].append((v - 1, w))
        edge[v - 1].append((u - 1, w))
    color = [-1] * n
    color[0] = 0
    stack = [0]
    while stack:
        now = stack.pop()
        for to, w in edge[now]:
            if color[to] != -1:
                continue
            if w % 2 == 0:
                color[to] = color[now]
            else:
                color[to] = 1 - color[now]
            stack.append(to)
    for c in color:
        print(c)
