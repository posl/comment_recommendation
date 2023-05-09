def check_star(n, edges):
    # check if all nodes except one have degree 1
    if len(edges) != n-1:
        return False
    degree = [0]*n
    for a, b in edges:
        degree[a-1] += 1
        degree[b-1] += 1
    if degree.count(1) != n-1:
        return False
    # check if the remaining node has degree n-1
    if degree.count(n-1) != 1:
        return False
    return True
