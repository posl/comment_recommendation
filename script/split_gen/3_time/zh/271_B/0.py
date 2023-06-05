def get_input():
    n,q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    s = []
    t = []
    for i in range(q):
        s_,t_ = map(int, input().split())
        s.append(s_)
        t.append(t_)
    return n,q,a,s,t
