def get_input():
    n, m = input().split()
    n = int(n)
    m = int(m)
    s = []
    c = []
    for i in range(m):
        s_i, c_i = input().split()
        s_i = int(s_i)
        c_i = int(c_i)
        s.append(s_i)
        c.append(c_i)
    return n, m, s, c
