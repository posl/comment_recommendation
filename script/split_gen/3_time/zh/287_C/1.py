def isPathGraph(num, edges):
    for i in range(1, num+1):
        if len(edges[i]) != 2:
            return "No"
    return "Yes"
