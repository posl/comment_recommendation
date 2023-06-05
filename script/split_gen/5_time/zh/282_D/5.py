def dfs(i, color):
    global flag
    global colors
    global visited
    # 如果已经找到了不合法的情况，就不用再找了
    if flag == 0:
        return
    # 如果已经访问过，就不用再访问了
    if visited[i] == 1:
        return
    # 如果当前点已经染色了，就看看和之前的颜色是否相同
    if colors[i] != 0:
        if colors[i] == color:
            # 如果颜色相同，就找到了不合法的情况
            flag = 0
        return
    # 如果当前点没有染色，就染上颜色
    colors[i] = color
    # 并且标记为已经访问
    visited[i] = 1
    # 然后遍历所有与当前点相邻的点
    for j in range(len(graph[i])):
        # 如果当前点和相邻的点颜色相同，就找到了不合法的情况
        if colors[graph[i][j]] == color:
            flag = 0
            return
        # 如果当前点和相邻的点颜色不同，就继续遍历相邻的点
        else:
            dfs(graph[i][j], -color)
