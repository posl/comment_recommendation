def get_edges(L):
    edges = []
    for i in range(L):
        edges.append([i+1,i+2,0])
    for i in range(2,L):
        edges.append([i,L+1,0])
    return edges
L = int(input())
edges = get_edges(L)
print(L+1,len(edges))
for edge in edges:
    print(*edge)
