def get_input():
    N, M = map(int, raw_input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, raw_input().split())
        s.append(s_i)
        c.append(c_i)
    return N, M, s, c
