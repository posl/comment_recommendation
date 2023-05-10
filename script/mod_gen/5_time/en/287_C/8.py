def check_path_graph(n, m, edges):
    if m != n - 1:
        return 'No'
    else:
        for i in range(n):
            if len(edges[i]) != 2:
                return 'No'
        return 'Yes'

if __name__ == '__main__':
    check_path_graph()