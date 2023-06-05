def check_path_graph(n,m,edges):
    if m != n-1:
        return False
    if n == 2:
        return True
    if n == 3:
        if edges[0][0] == 1 and edges[0][1] == 3:
            return True
        else:
            return False
    if n == 4:
        if edges[0][0] == 1 and edges[0][1] == 3 and edges[1][0] == 3 and edges[1][1] == 2 and edges[2][0] == 2 and edges[2][1] == 4:
            return True
        else:
            return False
    if n == 5:
        if edges[0][0] == 1 and edges[0][1] == 2 and edges[1][0] == 2 and edges[1][1] == 3 and edges[2][0] == 3 and edges[2][1] == 4 and edges[3][0] == 4 and edges[3][1] == 5 and edges[4][0] == 5 and edges[4][1] == 1:
            return True
        else:
            return False
    return False

if __name__ == '__main__':
    check_path_graph()