def get_data():
    n,m,q = map(int,input().split())
    l = []
    r = []
    for i in range(m):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    p = []
    q = []
    for i in range(q):
        p_i,q_i = map(int,input().split())
        p.append(p_i)
        q.append(q_i)
    return n,m,q,l,r,p,q
