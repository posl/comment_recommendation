def get_input():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r_c_list = []
    for i in range(n):
        r, c = map(int, input().split())
        r_c_list.append((r, c))
    q = int(input())
    d_l_list = []
    for i in range(q):
        d, l = input().split()
        d_l_list.append((d, int(l)))
    return h, w, r_s, c_s, n, r_c_list, q, d_l_list
