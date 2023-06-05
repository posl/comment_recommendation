def is_path_graph(n,m,edges):
    if m != n-1:
        return False
    for i in range(1,n+1):
        if len(edges[i]) != 2:
            return False
    return True

if __name__ == '__main__':
    is_path_graph()