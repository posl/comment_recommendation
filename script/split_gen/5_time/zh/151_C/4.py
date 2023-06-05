def get_input():
    n,m = input().split(' ')
    n = int(n)
    m = int(m)
    p = []
    s = []
    for i in range(m):
        p_i,s_i = input().split(' ')
        p_i = int(p_i)
        p.append(p_i)
        s.append(s_i)
    return n,m,p,s
