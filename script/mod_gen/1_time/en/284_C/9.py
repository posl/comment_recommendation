def find_connected_components(n, edges):
    if not edges:
        return n
    visited = [False] * (n + 1)
    visited[0] = True
    connected_components = 0
    for i in range(1, n + 1):
        if visited[i]:
            continue
        connected_components += 1
        stack = [i]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            for edge in edges:
                if edge[0] == node:
                    stack.append(edge[1])
                elif edge[1] == node:
                    stack.append(edge[0])
    return connected_components

if __name__ == '__main__':
    find_connected_components()