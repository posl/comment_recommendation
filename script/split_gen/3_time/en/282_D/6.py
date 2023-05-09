def main():
    n, m = map(int, input().split())
    nodes = [[] for i in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        nodes[u].append(v)
        nodes[v].append(u)
    colors = [0] * (n + 1)
    ans = 0
    for i in range(1, n + 1):
        if colors[i] != 0:
            continue
        colors[i] = 1
        stack = [i]
        while stack:
            node = stack.pop()
            for next_node in nodes[node]:
                if colors[next_node] == 0:
                    colors[next_node] = -colors[node]
                    stack.append(next_node)
                elif colors[next_node] == colors[node]:
                    ans += 1
    print(ans)
