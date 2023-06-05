def addEdge(u, v, w):
    global edges
    global edgeNum
    global nodes
    global nodeNum
    edges[edgeNum] = (u, v, w)
    nodes[u].append(edgeNum)
    nodes[v].append(edgeNum)
    edgeNum += 1
