def get_input():
    n = int(input())
    s_t_list = []
    for i in range(n):
        s_t_list.append(input().split())
    return n, s_t_list
