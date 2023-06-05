def get_edge_num():
    n,m = map(int,raw_input().split())
    edge_list = []
    for i in range(m):
        edge_list.append(map(int,raw_input().split()))
    return n,m,edge_list
