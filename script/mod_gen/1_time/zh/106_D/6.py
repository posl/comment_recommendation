def read_input():
    n,m,q = [int(x) for x in input().split()]
    l = []
    r = []
    for i in range(m):
        l_i,r_i = [int(x) for x in input().split()]
        l.append(l_i)
        r.append(r_i)
    p = []
    q = []
    for i in range(q):
        p_i,q_i = [int(x) for x in input().split()]
        p.append(p_i)
        q.append(q_i)
    return n,m,q,l,r,p,q

if __name__ == '__main__':
    read_input()