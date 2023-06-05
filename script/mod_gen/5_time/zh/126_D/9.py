def get_color(n,edges):
    """edges: list of tuple"""
    color = [None] * n
    color[0] = 0
    stack = [0]
    while stack:
        node = stack.pop()
        for edge in edges:
            if edge[0] == node:
                if color[edge[1]-1] is None:
                    color[edge[1]-1] = color[node] ^ edge[2] & 1
                    stack.append(edge[1]-1)
    return color

if __name__ == '__main__':
    get_color()