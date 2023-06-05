def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    color = [-1] * n
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if color[nv] == -1:
                color[nv] = 1 - color[v]
                stack.append(nv)
    color_num = [0, 0]
    for c in color:
        color_num[c] += 1
    ans = color_num[0] * color_num[1] - m
    print(ans)
