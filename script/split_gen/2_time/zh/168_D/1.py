def get_next_node(node, link, visited):
    for i in range(len(link)):
        if link[i][0] == node and link[i][1] not in visited:
            return link[i][1]
        elif link[i][1] == node and link[i][0] not in visited:
            return link[i][0]
    return 0
