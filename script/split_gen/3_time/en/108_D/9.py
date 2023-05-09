def generate_graph(L):
    current_length = 0
    edge_length = 0
    edges = []
    for i in range(1, L):
        edges.append([i, i + 1, edge_length])
        current_length += edge_length
        edge_length += 1
        if current_length == L:
            break
        elif current_length > L:
            edge_length -= 1
            current_length -= edge_length
            for j in range(i - 1, 0, -1):
                edges.append([j, j + 1, edge_length])
                current_length += edge_length
                edge_length += 1
                if current_length == L:
                    break
                elif current_length > L:
                    edge_length -= 1
                    current_length -= edge_length
                    break
    return edges
L = int(input())
edges = generate_graph(L)
print(len(edges) + 1, len(edges))
for edge in edges:
    print(*edge)
print(len(edges) + 1, 1, 0)
