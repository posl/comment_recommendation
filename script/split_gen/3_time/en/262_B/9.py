def count_triangles(edges):
    # count the number of triangles in a graph
    # edges is a list of tuples (a, b) representing edges
    count = 0
    for a, b in edges:
        for c, d in edges:
            if a == c and d != b:
                for e, f in edges:
                    if b == e and f == d:
                        count += 1
    return count
