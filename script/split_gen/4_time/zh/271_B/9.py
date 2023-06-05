def get_input():
    input_list = list(map(int, input().split()))
    N = input_list[0]
    Q = input_list[1]
    seq_list = []
    for i in range(N):
        seq_list.append(list(map(int, input().split())))
    query_list = []
    for i in range(Q):
        query_list.append(list(map(int, input().split())))
    return N, Q, seq_list, query_list
