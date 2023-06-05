def dfs(node, parent):
    for i in node:
        if i != parent:
            dfs(i, node)
            for j in range(len(node)):
                if node[j] == i:
                    node[j] = node[j] + node[i]
