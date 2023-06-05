def solve():
    # 树的节点数
    N = int(input())
    # 起点
    X = int(input())
    # 终点
    Y = int(input())
    # 边
    edges = []
    for i in range(N-1):
        edges.append(list(map(int, input().split())))
    # 顶点
    vertexs = []
    for i in range(N):
        vertexs.append([])
    # 顶点的子节点
    for edge in edges:
        vertexs[edge[0]-1].append(edge[1])
        vertexs[edge[1]-1].append(edge[0])
    # 顶点的父节点
    parents = [0] * N
    # 父节点的栈
    stack = []
    stack.append(1)
    while len(stack) > 0:
        vertex = stack.pop()
        for child in vertexs[vertex-1]:
            if child != parents[vertex-1]:
                parents[child-1] = vertex
                stack.append(child)
    # 起点到终点的路径
    path = []
    path.append(Y)
    while path[-1] != X:
        path.append(parents[path[-1]-1])
    # 输出
    for i in range(len(path)):
        print(path[len(path)-1-i], end=" ")
    print()
