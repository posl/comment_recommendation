def is_polygon(n, edges):
    edges.sort()
    if edges[-1] < sum(edges[:-1]):
        return '是'
    else:
        return '否'
