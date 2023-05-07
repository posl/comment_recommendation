def solve(N, edges):
    # 0: white, 1: black
    colors = [None] * N
    colors[0] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for u, w in edges[v]:
            if colors[u] is None:
                colors[u] = (colors[v] + w % 2) % 2
                stack.append(u)
    return colors
